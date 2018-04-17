# coding=utf-8
from setuptools import setup, find_packages
from os.path import realpath, dirname
from os import listdir


root_dir = dirname(realpath(__file__))
templates_dir = root_dir+'/flaskipy/flaskipy_templates'
# read readme file
with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()
# package data file
data_files = ['flaskipy/flaskipy_templates/'+file for file in listdir(templates_dir) if file.endswith(".txt")]

setup(
    name='flaskipy',
    version='0.1.0',
    python_requires='>3.0.0',
    packages = find_packages(
        include=['flaskipy'],
        exclude='tests'),
    include_package_data=True,
    data_files=[("flaskipy_templates", data_files)],  # package data files
    url='https://github.com/osmangoninahid/flaskipy',
    license='MIT License',
    author=[
        'Osman Goni Nahid',
        'Porimol Chandro'
    ],
    author_email=[
        'nirobshitol@gmail.com',
        'porimolchandroroy@gmail.com'
    ],
    description='Flaskipy is a cli tool for Flask',
    long_description=long_description,
    keywords = ['Flaskipy'],
    install_requires=[
        'Click',
        'flask',
        'inquirer',
        'inflect',
    ],
    entry_points='''
        [console_scripts]
        flaskipy=flaskipy.commands:cli
    ''',
)
