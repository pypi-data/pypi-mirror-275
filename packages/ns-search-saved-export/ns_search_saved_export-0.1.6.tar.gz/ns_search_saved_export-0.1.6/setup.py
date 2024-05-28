from setuptools import setup, find_packages

setup(
    name='ns_search_saved_export',
    version='0.1.6',
    description='A library for interacting with NetSuite API and exporting data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gildder',
    author_email='gildder@outlook.com',
    url='https://github.com/gildder/netsuite-search-saved-export',
    packages=find_packages(),
    install_requires=[
        'oauth2',
        'requests',
        'pandas',
        'setuptools',
        'openpyxl'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
