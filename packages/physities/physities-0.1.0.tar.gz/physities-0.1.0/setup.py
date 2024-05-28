# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['physities',
 'physities.src',
 'physities.src.dimension',
 'physities.src.scale',
 'physities.src.unit']

package_data = \
{'': ['*']}

install_requires = \
['kobject>=0.6.1,<0.7.0', 'pytest>=7.4.0,<8.0.0']

setup_kwargs = {
    'name': 'physities',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Physities\nRepresent physical quantities\n',
    'author': 'M4tus4l3m',
    'author_email': 'lucas.sievers@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
