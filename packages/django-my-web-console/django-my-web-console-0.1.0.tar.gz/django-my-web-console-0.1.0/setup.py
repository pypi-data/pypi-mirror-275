from setuptools import setup, find_packages

setup(
    name='django-my-web-console',
    version='0.1.0',
    description='A simple web console based on Django.',
    author='yuhua.yang',
    packages=find_packages(where='../console'),
)