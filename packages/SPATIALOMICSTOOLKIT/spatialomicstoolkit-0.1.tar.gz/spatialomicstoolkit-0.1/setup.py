
from setuptools import setup, find_packages

setup(
    name='SPATIALOMICSTOOLKIT',
    version='0.1',
    packages=find_packages(include=['utils','utils.viziumHD']),
    entry_points={
        'console_scripts': [
            'run_vizium=scripts.run_vizum:main',
        ],
    },
)