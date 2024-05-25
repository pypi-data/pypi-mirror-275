# setup.py

from setuptools import setup, find_packages

setup(
    name='rivalz-py-client',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python client for interacting with Rivalz API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/rivalz-py-client',
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.2',
        'python-dotenv>=1.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)