# setup.py
from setuptools import setup, find_packages

PACKAGE_NAME = 'ambient_edge_server'
VERSION = '0.1.1'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'fastapi==0.111.0',
        'pydantic==2.7.1',
        'ambient_event_bus_client==0.1.4',
        'ambient_backend_api_client==0.1.11',
    ],
    entry_points={
        'console_scripts': [
            'ambient_edge_server=ambient_edge_server.run:run',
        ],
    },
)
