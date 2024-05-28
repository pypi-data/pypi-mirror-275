from setuptools import setup, find_packages

setup(
    name='boolgen',
    version='1.1.0',
    packages=find_packages(),
    description='A library for generating and simplifying Boolean expressions from truth tables',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Schuyler Erle',
    author_email='schuyler@nocat.net',
    url='https://github.com/schuyler/boolgen',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'boolgen=boolgen:main',
        ],
    },
)
