from setuptools import setup, find_packages

setup(
    name='csv_identifier',
    version='0.1',
    description='A package to read CSV and assign unique IDs to a specified column',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
