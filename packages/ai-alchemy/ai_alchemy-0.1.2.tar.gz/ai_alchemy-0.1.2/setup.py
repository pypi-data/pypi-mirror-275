# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ai_alchemy', 'ai_alchemy.core']

package_data = \
{'': ['*']}

install_requires = \
['openai>=1.30.1,<2.0.0',
 'pandas>=2.2.2,<3.0.0',
 'pydantic>=2.7.1,<3.0.0',
 'requests>=2.31.0,<3.0.0']

setup_kwargs = {
    'name': 'ai-alchemy',
    'version': '0.1.2',
    'description': 'Lightweight package for arbitrary data transformation and validation using AI models and first class python libraries like Pandas and Pydantic.',
    'long_description': '',
    'author': 'Josh Mogil',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
