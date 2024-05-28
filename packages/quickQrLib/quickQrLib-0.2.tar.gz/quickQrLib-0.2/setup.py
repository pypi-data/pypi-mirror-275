from setuptools import setup, find_packages

setup(
    name='quickQrLib',
    version='0.2',
    packages=find_packages(),
    
    install_requires=[
        'djangorestframework-simplejwt==5.3.1',
    ]
)