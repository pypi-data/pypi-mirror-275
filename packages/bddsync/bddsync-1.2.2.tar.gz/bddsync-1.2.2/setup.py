from setuptools import setup


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bddsync',
    packages=['bddsync'],
    entry_points={
        "console_scripts": [
            "bddsync = bddsync.__main__:main"
        ],
    },
    version='1.2.2',
    license='MIT',
    description='Tools to synchronize BDD files with test management tools like Jira-Xray',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alejandro Manzanero',
    author_email='alejmans@gmail.com',
    url='https://github.com/Manzanero/bddsync',
    download_url='https://github.com/Manzanero/bddsync/archive/refs/tags/v1.2.2.tar.gz',
    keywords=['bdd', 'cucumber', 'behave', 'jira', 'xray', 'testing'],
    install_requires=[
        'requests',
        'PyYAML',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
