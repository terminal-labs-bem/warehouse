# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['warehouse',
 'warehouse.content',
 'warehouse.functions',
 'warehouse.ux']

package_data = \
{'': ['*'],
 'warehouse': ['assets/mocking/keys/*',
                 'assets/mocking/testdata/*',
                 'assets/static/*',
                 'assets/warehouses/*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'flask>=3.0.0,<4.0.0']

entry_points = \
{'console_scripts': ['warehouse = warehouse.ux.cli:cli']}

setup_kwargs = {
    'name': 'warehouse',
    'version': '0.0.1',
    'description': '',
    'long_description': '\n',
    'author': 'Michael Verhulst',
    'author_email': 'michael@terminallabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)

