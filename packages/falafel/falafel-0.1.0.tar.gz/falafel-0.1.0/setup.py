# falafel/setup.py

from setuptools import setup, find_packages

setup(
    name='falafel',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    url='https://github.com/yourusername/falafel',
    author='Mr.Falafel',
    author_email='your.email@example.com',
    description='A sample Python library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
