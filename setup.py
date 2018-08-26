from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Fetch long description from README
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read() # Read from README

# Basic project info
setup (
    # Name of project on pypi.org
    #
    # e.g. pip install CryptPy
    name='CryptPy',

    # Version
    #
    # e.g. pip install CryptPy >= 0.1.0
    version='0.1.0',

    # Short description fetched from GitHub page
    description='Dynamically programmable Python/JS botnet (educational purposes only).',


    # Longer description fetched from README
    #
    # Used in 'description' field on https://packaging.python.org/specifications/
    long_description=long_description,

    long_description_content_type='text/markdown',

    # Links to project homepage (github)
    #
    # TODO: Probably going to be replaced with a github.io page later
    url='https://github.com/mitsukomegumi/CryptPy.js',

    # Does this even need a comment? Probably not.
    author='Mitsuko Megumi, Matt Nappo',

    # 'My' email
    author_email='mitsukomegumii@gmail.com',

    classifiers=[
        # Obviously
        'Development Status :: 3 - Alpha',

        # Because this tool is just for 'educational' use
        'Intended Audience :: Developers',

        # Ree, GPL
        'License :: GPL-3.0 License',
        
        # Python 3
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    # Used for discovery, I guess
    keywords='botnet tools development python js javascript hacking hackerman imin',

    # Internal packages
    packages=find_packages(include=['networking', 'database', 'common', 'command', 'bot'])
)