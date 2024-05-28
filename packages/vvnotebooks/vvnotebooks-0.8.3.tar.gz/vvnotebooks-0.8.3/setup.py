# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vvnotebooks', 'vvnotebooks.snowflake']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=6.0.1,<7.0.0']

setup_kwargs = {
    'name': 'vvnotebooks',
    'version': '0.8.3',
    'description': 'Some useful Jupyter notebook abstractions',
    'long_description': 'vvnotebooks\n===========\n\nThis Python module defines some useful abstractions for\nwriting Jupyter notebooks with a more rigorous approach\nto the software engineering side.\n',
    'author': 'James Hunt',
    'author_email': 'james@niftylogic.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
