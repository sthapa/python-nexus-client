from setuptools import setup, find_packages

with open('requirements.txt') as reqs:
    install_requires = [line for line in reqs]

CONFIG = {
  'description':'client for Globus Nexus',
  'version':'0.0.3',
  'name':'nexus-client',
  'package_dir': {'':'lib'},
  'packages': ['nexus'],
  'install_requires': install_requires,
  'tests_require': ['nose', 'testfixtures'],
  'test_suite': 'tests',
}

setup(**CONFIG)
