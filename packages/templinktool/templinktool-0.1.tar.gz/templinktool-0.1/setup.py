# setup.py

from setuptools import setup, find_packages

setup(
    name='templinktool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'pyngrok',
        'werkzeug',
    ],
    entry_points={
        'console_scripts': [
            'linkm=main:main',      # linkm-start commandmmand
        ],
    },
)
