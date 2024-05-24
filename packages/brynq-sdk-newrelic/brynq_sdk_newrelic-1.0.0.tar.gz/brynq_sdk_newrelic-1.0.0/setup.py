from setuptools import setup

setup(
    name='brynq_sdk_newrelic',
    version='1.0.0',
    description='Newrelic wrapper from BrynQ',
    long_description='Newrelic wrapper from BrynQ',
    author='BrynQ',
    author_email='support@brynq.com',
    packages=["brynq_sdk.newrelic"],
    license='BrynQ License',
    install_requires=[
        'brynq-sdk-brynq>=1',
        'pandas>=2,<3'
    ],
    zip_safe=False,
)
