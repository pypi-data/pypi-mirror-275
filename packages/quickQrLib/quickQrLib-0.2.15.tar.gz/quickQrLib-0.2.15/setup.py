from setuptools import setup, find_packages
setup(
    name='quickQrLib',
    version='0.2.15',
    packages=find_packages(),
    
    install_requires=[
        'djangorestframework-simplejwt==5.3.1',
        'django==5.0.6',
        'boto3==1.34.113'
    ]
)
