# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['scida',
 'scida.configfiles',
 'scida.configfiles.units',
 'scida.customs',
 'scida.customs.arepo',
 'scida.customs.arepo.MTNG',
 'scida.customs.arepo.TNGcluster',
 'scida.customs.gadgetstyle',
 'scida.customs.gizmo',
 'scida.customs.rockstar',
 'scida.customs.swift',
 'scida.interfaces.mixins',
 'scida.io']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=5.0,<6.0',
 'dask[array,dataframe,distributed]>=2023,<2024',
 'distributed>=2023,<2024',
 'h5py>=3.7.0,<4.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'numba>=0.57,<0.58',
 'numpy>=1.21,<2.0',
 'pint>=0.22,<0.23',
 'pyyaml>=5.3.1',
 'requests>=2.31.0,<3.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'zarr>=v2.10.0,<3.0.0']

setup_kwargs = {
    'name': 'scida',
    'version': '0.3.2',
    'description': 'Convenience wrapper around large scientific datasets to process with dask.',
    'long_description': '# scida\n\n![test status](https://github.com/cbyrohl/scida/actions/workflows/tests.yml/badge.svg)\n[![DOI](https://joss.theoj.org/papers/10.21105/joss.06064/status.svg)](https://doi.org/10.21105/joss.06064)\n\nscida is an out-of-the-box analysis tool for large scientific datasets. It primarily supports the astrophysics community, focusing on cosmological and galaxy formation simulations using particles or unstructured meshes, as well as large observational datasets.\nThis tool uses dask, allowing analysis to scale up from your personal computer to HPC resources and the cloud.\n\n## Features\n\n- Unified, high-level interface to load and analyze large datasets from a variety of sources.\n- Parallel, task-based data processing with dask arrays.\n- Physical unit support via pint.\n- Easily extensible architecture.\n\n## Requirements\n\n- Python 3.9, 3.10, 3.11\n\n\n## Documentation\nThe documentation can be found [here](https://cbyrohl.github.io/scida/).\n\n## Install\n\n```\npip install scida\n```\n\n## First Steps\n\nAfter installing scida, follow the [tutorial](https://cbyrohl.github.io/scida/tutorial/).\n\n## Citation\n\nIf you use scida in your research, please cite the following [paper](https://joss.theoj.org/papers/10.21105/joss.06064):\n\n```text\n`Byrohl et al., (2024). scida: scalable analysis for scientific big data. Journal of Open Source Software, 9(94), 6064, https://doi.org/10.21105/joss.06064`\n```\n\nwith the following bibtex entry:\n\n```text\n@article{scida,\n  title = {scida: scalable analysis for scientific big data},\n  author = {Chris Byrohl and Dylan Nelson},\n  doi = {10.21105/joss.06064},\n  url = {https://doi.org/10.21105/joss.06064}, year = {2024},\n  publisher = {The Open Journal}, volume = {9}, number = {94},\n  pages = {6064},\n  journal = {Journal of Open Source Software}\n}\n```\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue](https://github.com/cbyrohl/scida/issues/new) along with a detailed description.\n\n## License\n\nDistributed under the terms of the [MIT license](LICENSE),\n_scida_ is free and open source software.\n',
    'author': 'Chris Byrohl',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
