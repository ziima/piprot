import sys, os
from setuptools import setup

"""
Use pandoc to convert README.md to README.rst before uploading
   pandoc README.md -o README.rst
"""


if 'publish' in sys.argv:
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

INSTALL_REQUIRES = open('requirements.txt').read().splitlines()


setup(
    name='piprot',
    version='0.9.10',
    author='Brenton Cleeland',
    author_email='brenton@brntn.me',
    packages=['piprot', 'piprot.providers'],
    url='http://github.com/sesh/piprot',
    license='MIT License',
    description='How rotten are your requirements?',
    long_description='',
    entry_points={
        'console_scripts': [
            'piprot = piprot.piprot:piprot',
        ]
    },
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
