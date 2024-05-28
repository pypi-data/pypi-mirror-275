"""
Python SDK external package setup
"""

# Imports
from setuptools import setup, find_packages

# Setup
setup(
    name='panda_server_sdk',
    version='1.1.0',
    description='Python SDK for Panda Server',
    packages=find_packages(include=['panda_server_sdk', 'panda_server_sdk.*'])
)
