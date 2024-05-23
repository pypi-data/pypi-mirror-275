# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sed',
 'sed.binning',
 'sed.calibrator',
 'sed.core',
 'sed.io',
 'sed.loader',
 'sed.loader.base',
 'sed.loader.flash',
 'sed.loader.generic',
 'sed.loader.mpes',
 'sed.loader.sxp']

package_data = \
{'': ['*'], 'sed': ['config/*']}

install_requires = \
['bokeh>=2.4.2',
 'dask>=2021.12.0',
 'fastdtw>=0.3.4',
 'fastparquet>=0.8.0',
 'h5py>=3.6.0',
 'ipympl>=0.9.1',
 'ipywidgets>=7.7.1,<8.0.0',
 'joblib>=1.2.0',
 'lmfit>=1.0.3',
 'matplotlib>=3.5.1',
 'natsort>=8.1.0',
 'numba>=0.55.1',
 'numpy>=1.18',
 'opencv-python>=4.8.0.74',
 'pandas>=1.4.1',
 'psutil>=5.9.0',
 'pyarrow>=14.0.1',
 'pynxtools-mpes>=0.0.3',
 'pynxtools>=0.3.1',
 'pyyaml>=6.0.0',
 'scipy>=1.8.0',
 'symmetrize>=0.5.5',
 'threadpoolctl>=3.1.0',
 'tifffile>=2022.2.9',
 'tqdm>=4.62.3',
 'xarray>=0.20.2']

extras_require = \
{':extra == "notebook"': ['jupyterlab-h5web[full]>=8.0.0,<9.0.0'],
 'notebook': ['jupyter>=1.0.0', 'ipykernel>=6.9.1', 'jupyterlab>=3.4.0,<4.0.0']}

setup_kwargs = {
    'name': 'sed-processor',
    'version': '0.1.10a3',
    'description': 'Single Event Data Frame Processor: Backend to handle photoelectron resolved datastreams',
    'long_description': '[![Documentation Status](https://github.com/OpenCOMPES/sed/actions/workflows/documentation.yml/badge.svg)](https://opencompes.github.io/sed/)\n[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)\n![](https://github.com/OpenCOMPES/sed/actions/workflows/linting.yml/badge.svg?branch=main)\n![](https://github.com/OpenCOMPES/sed/actions/workflows/testing_multiversion.yml/badge.svg?branch=main)\n![](https://img.shields.io/pypi/pyversions/sed-processor)\n![](https://img.shields.io/pypi/l/sed-processor)\n[![](https://img.shields.io/pypi/v/sed-processor)](https://pypi.org/project/sed-processor)\n[![Coverage Status](https://coveralls.io/repos/github/OpenCOMPES/sed/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/OpenCOMPES/sed?branch=main)\n\nBackend to handle photoelectron resolved datastreams.\n\n# Installation\n\n## Pip (for users)\n\n- Create a new virtual environment using either venv, pyenv, conda, etc. See below for an example.\n\n```bash\npython -m venv .sed-venv\n```\n\n- Activate your environment:\n\n```bash\nsource .sed-venv/bin/activate\n```\n\n- Install `sed`, distributed as `sed-processor` on PyPI:\n\n```bash\npip install sed-processor\n```\n\n- This should install all the requirements to run `sed` in your environment.\n\n- If you intend to work with Jupyter notebooks, it is helpful to install a Jupyter kernel for your environment. This can be done, once your environment is activated, by typing:\n\n```bash\npython -m ipykernel install --user --name=sed_kernel\n```\n## For Contributors\n\nTo contribute to the development of `sed`, you can follow these steps:\n\n1. Clone the repository:\n\n```bash\ngit clone https://github.com/OpenCOMPES/sed.git\ncd sed\n```\n\n2. Install the repository in editable mode:\n\n```bash\npip install -e .\n```\n\nNow you have the development version of `sed` installed in your local environment. Feel free to make changes and submit pull requests.\n\n## Poetry (for maintainers)\n\n- Prerequisites:\n  + Poetry: https://python-poetry.org/docs/\n\n- Create a virtual environment by typing:\n\n```bash\npoetry shell\n```\n\n- A new shell will be spawned with the new environment activated.\n\n- Install the dependencies from the `pyproject.toml` by typing:\n\n```bash\npoetry install --with dev, docs\n```\n\n- If you wish to use the virtual environment created by Poetry to work in a Jupyter notebook, you first need to install the optional notebook dependencies and then create a Jupyter kernel for that.\n\n  + Install the optional dependencies `ipykernel` and `jupyter`:\n\n  ```bash\n  poetry install -E notebook\n  ```\n\n  + Make sure to run the command below within your virtual environment (`poetry run` ensures this) by typing:\n\n  ```bash\n  poetry run ipython kernel install --user --name=sed_poetry\n  ```\n\n  + The new kernel will now be available in your Jupyter kernels list.\n',
    'author': 'OpenCOMPES team',
    'author_email': 'sed-processor@mpes.science',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/OpenCOMPES/sed',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11.9',
}


setup(**setup_kwargs)
