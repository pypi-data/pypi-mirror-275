from setuptools import setup, find_packages

setup(
    name='techtribe-addressbook',
    version='1.0.0',
    description='Save your data easy and convenient',
    url='https://github.com/Oldestgraf/TechTribe',
    packages=find_packages(),
    install_requires=[
        'prompt-toolkit==3.0.43',
        'wcwidth==0.2.13',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
