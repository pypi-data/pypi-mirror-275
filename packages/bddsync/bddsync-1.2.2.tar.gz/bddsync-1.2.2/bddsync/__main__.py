import argparse
import glob
import os
import shlex
import sys

import yaml
from bddsync.cucumber_wrapper import CucumberWrapper
from bddsync.xray_wrapper import XrayWrapper

NAME = 'bddsync'
VERSION = 'v1.2.2'


class Commands:
    TEST_REPOSITORY_FOLDERS = 'test-repository-folders'
    FEATURES = 'features'
    SCENARIOS = 'scenarios'
    UPLOAD_FEATURES = 'upload-features'
    UPLOAD_RESULTS = 'upload-results'
    GENERATE_DOCS = 'generate-docs'

    @classmethod
    def all(cls):
        return [i[1] for i in cls.__dict__.items() if not i[0].startswith('_') and isinstance(i[1], str)]


def get_credentials(args) -> [str, str]:
    if args.test_repository_user:
        test_repository_user = args.user
    elif 'TEST_REPOSITORY_USER' in dict(os.environ):
        test_repository_user = os.environ['TEST_REPOSITORY_USER']
    else:
        test_repository_user = input('Enter repository user (or set TEST_REPOSITORY_USER environment variable): ')

    if args.test_repository_pass:
        test_repository_pass = args.user
    elif 'TEST_REPOSITORY_PASS' in dict(os.environ):
        test_repository_pass = os.environ['TEST_REPOSITORY_PASS']
    else:
        test_repository_pass = input('Enter repository pass (or set TEST_REPOSITORY_PASS environment variable): ')

    if not test_repository_user or not test_repository_pass:
        print('Invalid credentials')

    return test_repository_user, test_repository_pass


def main(arg_vars: list = None):
    arg_vars = (shlex.split(arg_vars) if isinstance(arg_vars, str) else arg_vars) if arg_vars else sys.argv[1:]

    bddsync_args = []
    command = None
    command_args = None
    for var in arg_vars:
        bddsync_args.append(var)
        if var in Commands.all():
            command = var
            command_args = arg_vars[arg_vars.index(command) + 1:]
            break
    else:
        bddsync_args = ['-h']

    parser = argparse.ArgumentParser(NAME, description=VERSION)
    parser.add_argument('--config', default='bddfile.yml')
    parser.add_argument('-u', '--test-repository-user')
    parser.add_argument('-p', '--test-repository-pass')
    parser.add_argument('command', choices=Commands.all())
    args = parser.parse_args(bddsync_args)

    # config
    with open(args.config, 'r', encoding='utf-8') as kwarg_file:
        config = yaml.safe_load(kwarg_file)

    # add credentials to config
    config['test_repository_user'], config['test_repository_pass'] = get_credentials(args)

    if command == Commands.TEST_REPOSITORY_FOLDERS:
        test_repository_folders_command(command_args, config)
    elif command == Commands.FEATURES:
        features_command(command_args, config)
    elif command == Commands.SCENARIOS:
        scenarios_command(command_args, config)
    elif command == Commands.UPLOAD_FEATURES:
        upload_features_command(command_args, config)
    elif command == Commands.UPLOAD_RESULTS:
        upload_results_command(command_args, config)
    elif command == Commands.GENERATE_DOCS:
        generate_docs_command(command_args, config)
    else:
        print(f'Error: command "{command}" not managed yet')
        exit(1)


def test_repository_folders_command(command_args, config):
    parser = argparse.ArgumentParser(f"{NAME} [...] {Commands.TEST_REPOSITORY_FOLDERS}")
    parser.add_argument('--folder', default='/', help='folder to filter, else from root')
    args = parser.parse_args(command_args)

    xray = XrayWrapper(config)
    folders = xray.get_test_repository_folders(args.folder)
    for folder in folders:
        print(folder)


def features_command(command_args, config):
    parser = argparse.ArgumentParser(f"{NAME} [...] {Commands.FEATURES}")
    parser.parse_args(command_args)

    cucumber = CucumberWrapper(config)
    for feature in cucumber.features:
        print(f'{feature.name} (path="{feature.path}")')


def scenarios_command(command_args, config):
    parser = argparse.ArgumentParser(f"{NAME} [...] {Commands.SCENARIOS}")
    parser.parse_args(command_args)

    cucumber = CucumberWrapper(config)
    for feature in cucumber.features:
        for scenario in feature.scenarios:
            print(f'{scenario.name} (feature="{feature.name}")')


def upload_features_command(command_args, config):
    parser = argparse.ArgumentParser(f"{NAME} [...] {Commands.UPLOAD_FEATURES}")
    parser.add_argument('feature', nargs='+')
    args = parser.parse_args(command_args)
    paths = args.feature

    cucumber = CucumberWrapper(config)

    feature_paths = set()
    for path in paths:
        path = path.replace(os.sep, '/')
        globs = glob.glob(path, recursive=True) + glob.glob(os.path.join(path, '**'), recursive=True)
        [feature_paths.add(f.replace(os.sep, '/')) for f in globs if f.endswith('.feature')]
    feature_paths = list(sorted(feature_paths))

    features = []
    for feature_path in feature_paths:
        features += cucumber.get_features(feature_path)

    if not features:
        print('No features found')
        exit(0)

    xray = XrayWrapper(config)

    # check if there are test with the same name, or id is invalid
    total_errors = []
    errors = []
    for feature in features:
        issues = xray.get_issues_by_names([x.name.lower() for x in feature.scenarios])
        for scenario in feature.scenarios:
            occurrences = [issue['key'] for issue in issues if scenario.name == issue['fields']['summary']]

            if not scenario.test_id and occurrences:
                errors.append(f"{scenario.name} has no id but already exists in test repository {occurrences}")
            elif scenario.test_id:
                if not occurrences:
                    errors.append(f"{scenario.name} [{scenario.test_id}] "
                                  f"has different name in test repository")
                elif len(occurrences) == 1 and scenario.test_id != occurrences[0]:
                    errors.append(f"{scenario.name} [{scenario.test_id}] "
                                  f"has wrong id in test repository {occurrences}")
                elif len(occurrences) > 1:
                    errors.append(f"{scenario.name} [{scenario.test_id}] "
                                  f"has duplicated names in test repository {occurrences}")
        if errors:
            print(f'Errors in feature: {feature.name} (path="{feature.path}")')
            print(''.join([f" * {error}\n" for error in errors]), end='')
            total_errors += errors
            errors.clear()

    if total_errors:
        print("\nUpload stopped due to errors")
        exit(1)

    duplicates = []
    for feature in features:
        print(f'Uploading feature: {feature.name} (path="{feature.path}")')
        new_scenario_ids = xray.import_feature(feature)
        for i, scenario in enumerate(feature.scenarios):
            new_scenario_id = new_scenario_ids[i]
            if not scenario.test_id:
                scenario.test_id = new_scenario_id
                print(f' * Created Test: "{scenario.name}" [{scenario.test_id}]')
            elif scenario.test_id == new_scenario_id:
                print(f' * Updated Test: "{scenario.name}" [{scenario.test_id}]')
            else:
                duplicate = f' * Duplicated Test: "{scenario.name}" [{scenario.test_id}] -> ' \
                            f'check if this key has to be removed: [{new_scenario_id}]'
                print(duplicate)
                duplicates.append(duplicate)
                continue

            issues = xray.get_issue(new_scenario_id,
                                    ['labels', 'status', xray.test_repository_path_field, xray.test_plans_field])

            # manage labels
            labels = issues['fields']['labels']
            labels_to_remove = [scenario.test_id] + [label for label in labels if label not in scenario.effective_tags]
            xray.remove_labels(new_scenario_id, labels_to_remove)
            if labels_to_add := [tag for tag in feature.tags if tag not in scenario.effective_tags]:
                xray.add_labels(new_scenario_id, labels_to_add)

            # manage path
            test_dir = issues['fields'][xray.test_repository_path_field]
            if scenario.test_dir and scenario.test_dir != test_dir:
                xray.make_dirs(scenario.test_dir)
                xray.move_test_dir(new_scenario_id, scenario.test_dir)

            # manage plans
            tracked_test_plans = list(config.get('test_plans', {}).values())
            in_xray_test_plans = issues['fields'][xray.test_plans_field]
            in_code_test_plans = [plan.id for plan in scenario.test_plans]
            in_code_test_plans_to_add = [plan for plan in in_code_test_plans if plan not in in_xray_test_plans]
            in_code_test_plans_to_add = [plan for plan in in_code_test_plans_to_add if plan in tracked_test_plans]
            in_xray_test_plans_to_remove = [plan for plan in in_xray_test_plans if plan not in in_code_test_plans]
            in_xray_test_plans_to_remove = [plan for plan in in_xray_test_plans_to_remove if plan in tracked_test_plans]
            xray.add_tests_to_test_plans([new_scenario_id], in_code_test_plans_to_add)
            xray.remove_tests_from_test_plans([new_scenario_id], in_xray_test_plans_to_remove)

        print('Repairing feature tags')
        feature.repair_tags()
        print(f'Feature updated: {feature.name}\n')

    if duplicates:
        print("Check these duplicated tests:")
        for duplicate in duplicates:
            print(duplicate)
        exit(1)

    print(f'Process finished successfully\n')


def upload_results_command(command_args, config):
    parser = argparse.ArgumentParser(f"{NAME} [...] {Commands.UPLOAD_RESULTS}")
    parser.add_argument('-n', '--name', help='name of test execution')
    parser.add_argument('-e', '--environments', help='comma separated environment names')
    parser.add_argument('-f', '--fix-versions', help='comma separated fix versions')
    parser.add_argument('-p', '--test-plans', help='comma separated test plans IDs')
    parser.add_argument('-l', '--labels', help='comma separated labels')
    parser.add_argument('result', nargs='?')
    args = parser.parse_args(command_args)

    summary = args.name
    environments = args.environments.split(',') if args.environments else None
    fix_versions = args.fix_versions.split(',') if args.fix_versions else None
    test_plan_keys = args.test_plans.split(',') if args.test_plans else None
    labels = args.labels.split(',') if args.labels else None
    path = args.result

    # check environments
    if environments and 'test_environments' in config:
        test_environments = []
        for environment in environments:
            if environment in config['test_environments'].values():
                test_environments.append(environment)
            elif environment in config['test_environments']:
                test_environments.append(config['test_environments'][environment])
            else:
                print('Not valid test environment')
                exit(1)
    else:
        test_environments = environments
    if not test_environments and 'execution_test_environments' in config['required']:
        print(f"Execution test environment is required for this project {config['test_environments']}")
        print("use the flag: --environments ENVIRONMENT")
        exit(1)

    # check fix version
    if not fix_versions and 'execution_fix_version' in config['required']:
        print(f"Execution fix version is required for this project")
        print("use the flag: --fix-versions FIX_VERSION")
        exit(1)

    # check test plan
    if not test_plan_keys and 'execution_test_plans' in config['required']:
        print(f"Execution test plan is required for this project")
        print("use the flag: --test-plans TEST_PLAN")
        exit(1)

    # check result
    result_path = path or config['result']
    if not os.path.isfile(result_path):
        print(f'No results found in selected path {result_path}')
        exit(1)

    xray = XrayWrapper(config)
    print(f'Uploading result (path="{result_path}")')
    if test_plan_keys:
        print(f'Adding result to test plans {test_plan_keys}')
    test_execution = xray.import_result(result_path, summary, test_environments, fix_versions, test_plan_keys, labels)
    print(f" * Created Test Execution [{test_execution['key']}] "
          f"(url={xray.base_url}/browse/{test_execution['key']})")


def generate_docs_command(command_args, config):
    parser = argparse.ArgumentParser(f"{NAME} [...] {Commands.GENERATE_DOCS}")
    parser.parse_args(command_args)

    cucumber = CucumberWrapper(config)

    def get_desc(body):
        desc_body = []
        for line in body:
            line = line.strip()
            if line.startswith('Given'):
                break
            if line:
                desc_body.append(line)
        return ' '.join(desc_body)

    for feature in cucumber.features:
        feature_tags = ''.join([' @' + x for x in feature.tags])
        feature_desc = get_desc(feature.body)
        if feature_desc:
            print(f'- {feature.name}: {feature_desc}{feature_tags} > {feature.path}')
        else:
            print(f'- {feature.name}{feature_tags} > {feature.path}')

        for scenario in feature.scenarios:
            scenario_tags = ''.join([' @' + x for x in scenario.tags])
            scenario_desc = get_desc(scenario.body)
            if scenario_desc:
                print(f'  * {scenario.name}: {scenario_desc}{scenario_tags}')
            else:
                print(f'  * {scenario.name}{scenario_tags}')

        print()


if __name__ == '__main__':
    pass
    main(['-h'])
    # main(['-h', Commands.TEST_REPOSITORY_FOLDERS])
    # main(['-h', '--config', 'bddfile.yml', Commands.TEST_REPOSITORY_FOLDERS])
    # main(['-h', '--config', 'bddfile.yml', Commands.TEST_REPOSITORY_FOLDERS, '-h'])
    # main(['-h', '--config', 'bddfile.yml', Commands.TEST_REPOSITORY_FOLDERS, '-h', '--folder', '/FOLDER'])
    #
    # main([Commands.TEST_REPOSITORY_FOLDERS, '-h'])
    # main([Commands.TEST_REPOSITORY_FOLDERS])
    # main([Commands.TEST_REPOSITORY_FOLDERS, '-h', '--folder', '/FOLDER'])
    #
    # main([Commands.FEATURES, '-h'])
    # main([Commands.FEATURES])
    #
    # main([Commands.SCENARIOS, '-h'])
    # main([Commands.SCENARIOS])

    # main([Commands.UPLOAD_FEATURES, '-h'])
    # main([Commands.UPLOAD_FEATURES, 'features/**/sentinel*'])

    # main([Commands.UPLOAD_RESULTS, '-h'])
    # main([Commands.UPLOAD_RESULTS, '-e', 'ENV', '-f', 'RELEASE', '-p', 'ABC-1234'])
    # main([Commands.UPLOAD_RESULTS, 'output/result.json'])

    # main([Commands.GENERATE_DOCS, '-h'])
    # main([Commands.GENERATE_DOCS])
