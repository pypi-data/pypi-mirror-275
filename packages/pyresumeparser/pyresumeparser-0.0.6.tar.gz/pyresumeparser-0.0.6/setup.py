import os
from setuptools import setup, find_packages

setup(
    name='pyresumeparser',
    version='0.0.6',
    packages=find_packages(),
    install_requires=[
        'pdfminer.six==20231228',
        'spacy==3.7.4',
        'spacy-transformers==1.3.5',
        'tqdm==4.66.4'
    ],
    extras_require={
        'dev': [
            'build',
            'twine'
        ]
    },
    entry_points={
        'console_scripts': [
            'pyresumeparser=pyresumeparser.main:main',
        ],
    },
    author='Palash Khan',
    author_email='palashkhan777@gmail.com',
    description='A package for parsing resume and extracting entities.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pkhan123/pyresumeparser',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
