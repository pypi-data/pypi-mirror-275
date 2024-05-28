from setuptools import setup, find_packages
setup(
    name='quickQrLib',
    version='0.2.24',
    packages=find_packages(),
    install_requires=[
        'djangorestframework-simplejwt',
        'django',
        'boto3',
        'python-dateutil',
        'pytz'
    ],
)
