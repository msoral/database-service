# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "database_service"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Database Service",
    author_email="m.oral@blueflow.ai",
    url="",
    keywords=["Swagger", "Database Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['database_service=database_service.__main__:main']},
    long_description="""\
    Use this service to interact with the database. Always send the exchange name in the header of the request. All get/delete requests parameters are query parameters. All post/put request parameters are sent in the body of the request in json format. 
    """
)
