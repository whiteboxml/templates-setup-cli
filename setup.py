import setuptools

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

requirements = [
   'click',
],

setuptools.setup(
    name='custom_project',
    version='0.0.1',
    author='WhiteBoxᴹᴸ',
    author_email='info@whiteboxml.com',
    description='',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        custom_project=custom_project.cli:cli
    ''',
)
