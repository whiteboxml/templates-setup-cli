from setuptools import find_packages, setup

setup(
    name='custom_project',
    version='0.1',
    author='WhiteBox Machine Learning',
    description='',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        custom_project=custom_project.scripts.cli:cli
    ''',
)
