# coding: utf-8

import sys

from setuptools import find_packages, setup

NAME = "api"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion>=2.0.2", "swagger-ui-bundle>=0.0.2", "python_dateutil>=2.6.0"]

setup(
    name=NAME,
    version=VERSION,
    description="Database Service",
    author_email="m.oral@blueflow.ai",
    url="",
    keywords=["OpenAPI", "Database Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={"specification": ["openapi/openapi.yaml"]},
    include_package_data=True,
    entry_points={"console_scripts": ["api=api.__main__:main"]},
    long_description="""\
    Use this service to interact with the database. Always send the exchange name in the header of the request. All get/delete requests parameters are query parameters. All post/put request parameters are sent in the body of the request in json format. 
    """,
)
