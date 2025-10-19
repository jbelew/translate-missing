import os
from setuptools import setup, find_packages

setup(
    name='translate-missing',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'deep_translator',
    ],
    entry_points={
        'console_scripts': [
            'translate-missing=translate_missing.translate_missing:main',
        ],
    },
    author='John Belew',
    author_email='john.belew@gmail.com',
    description='A simple tool to find and translate missing keys in i18next localization files.',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/jbelew/translate-missing',
    license='GPL-3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
