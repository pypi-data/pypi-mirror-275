from setuptools import setup, find_packages

setup(
    name='piptoolpeteryang',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'piptool = piptool.main:main',
        ],
    },
)