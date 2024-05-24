from setuptools import setup, find_packages

setup(
    name='piptoolpeteryang',
    version='0.2',
    description='A tool to manage python dependencies',
    author='Peter Yang',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'piptool = piptool.main:main',
        ],
    },
)