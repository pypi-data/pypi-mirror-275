# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taurex_madhuseager2009']

package_data = \
{'': ['*']}

install_requires = \
['taurex>=3.1.1a0,<4.0.0']

entry_points = \
{'console_scripts': ['MadhuSeager2009 = MadhuSeager2009.__main__:main'],
 'taurex.plugins': ['taurex_MadhuSeager2009 = MadhuSeager2009.taurex']}

setup_kwargs = {
    'name': 'taurex-madhuseager2009',
    'version': '0.0.1',
    'description': 'MadhuSeager2009',
    'long_description': '# MadhuSeager2009: a TauREx 3.1 plugin to replicate the Madhusudhan Seager 2009 temperature-pressure profile\n\n## Requirements\n\n- You will need a working installation of TauREx 3.1 on your machine or computer server, with associated required Python packages: https://taurex3-public.readthedocs.io/\n\n## Installation\n\nYou can install _MadhuSeager2009_ with PyPi:\n\n```console\npip install taurex-madhuseager2009\n```\n\nYou can install _MadhuSeager2009_ by cloning this Github and installing via the terminal. This is done by:\n\nCloning the directory using:\n\n```console\n$ git clone https://github.com/michellebieger/MadhuSeager2009\n```\n\nMove into the downloaded folder:\n\n```console\n$ cd MadhuSeager2009\n```\n\nInstall by then typing in:\n\n```console\n$ pip install .\n```\n\nYou can check the installation by importing the plugin into Python:\n\n```console\n$ python -c "import MadhuSeager2009"\n```\n\nTo check that TauREx 3.1 has correctly registered your plugin:\n\n```console\n$ taurex --plugins\n```\n\nIf there are no errors, you have been successful!\n\n## Usage\n\nYou can use the ExampleNotebook in the repository, which runs this PT profile with TauREx as a forward model in a Jupyter Notebook. You can further modify the Notebook and include retrievals if desired.\n\nTo use the MadhuSeager2009 PT profile in a `.par` file and run TauREx on a command line, you can call the profile with either the keywords \'MadhuSeager2009\' or \'madhuseager2009\' under the "[Temperature]" parameter:\n\n```console\n$ profile_type = MadhuSeager2009\n```\n\nAn example `.par` file exists in this repository with all the parameters relevant to this PT profile--just add in your desired values/further parameters as normal when using TauREx and any other TauREx plugins.\n\n## License\n\nDistributed under the terms of the [GPL 3.0 license][license],\n_MadhuSeager2009_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems, please email michellebieger@live.com with a detailed description of the issue.\n',
    'author': 'M. F. Bieger',
    'author_email': 'mb987@exeter.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/michellebieger/MadhuSeager2009',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
