# setup.py

from setuptools import setup, find_packages

setup(
    name='templinktool',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
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
    author='sdidd',
    author_email='sdiddtayade@gmail.com',
    description='Creates a temporary server to share files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sdidd/templinkMaker.git',
    license='MIT',
)
