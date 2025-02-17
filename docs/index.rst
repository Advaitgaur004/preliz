Exploring and eliciting probability distributions
===================================================

|PyPI version|
|Tests|
|Coverage|
|Black|
|DOI|

.. |PyPI version| image:: https://badge.fury.io/py/preliz.svg
    :target: https://badge.fury.io/py/preliz
  
.. |Tests| image:: https://github.com/arviz-devs/preliz/actions/workflows/test.yml/badge.svg
    :target: https://github.com/arviz-devs/preliz

.. |Coverage| image:: https://codecov.io/gh/arviz-devs/preliz/branch/main/graph/badge.svg?token=SLJIK2O4C5 
    :target: https://codecov.io/gh/arviz-devs/preliz

.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

.. |DOI| image:: https://joss.theoj.org/papers/10.21105/joss.05499/status.svg
   :target: https://doi.org/10.21105/joss.05499


Overview
========

Prior elicitation refers to the process of transforming the knowledge of a particular domain into well-defined probability distributions.
Specifying useful priors is a central aspect of Bayesian statistics. PreliZ is a Python package aimed at helping practitioners choose prior
distributions by offering a set of tools for the various facets of prior elicitation. It covers a range of methods, from unidimensional prior
elicitation on the parameter space to predictive elicitation on the observed space. The goal is to be compatible with probabilistic programming
languages (PPL) in the Python ecosystem like PyMC and PyStan, while remaining agnostic of any specific PPL.

A good companion for PreliZ is `PriorDB <https://n-kall.github.io/priorDB/>`_, a database of prior distributions for Bayesian analysis. 
It is a community-driven project that aims to provide a comprehensive collection of prior distributions for a wide range of models and applications. 

**The Zen of PreliZ**

* Being open source, community-driven, diverse and inclusive.
* Avoid fully-automated solutions, keep the human in the loop.
* Separate tasks between humans and computers, so users can retain control of important decisions while numerically demanding, error-prone or tedious tasks are automatized.
* Prevent users to become overconfident in their own opinions.
* Easily integrate with other tools.
* Allow predictive elicitation.
* Having a simple and intuitive interface suitable for non-specialists in order to minimize cognitive biases and heuristics.
* Switching between different types of visualization such as kernel density estimates plots, quantile dotplots, histograms, etc. 
* Being agnostic of the underlying probabilistic programming language.
* Being modular.

Examples
========

.. toctree::
   :maxdepth: 2

   examples
   gallery_content

References
==========

.. toctree::
   :maxdepth: 1

   api_reference
   changelog

Installation
============

PreliZ is tested on Python 3.11+. And depends on ArviZ, matplotlib, NumPy, and SciPy. See `pyproject.toml <https://github.com/arviz-devs/preliz/blob/main/pyproject.toml>`_ for version information.


For the latest release, you can install PreliZ either using pip or conda-forge:

Using pip
---------

.. code-block:: bash

  pip install preliz

To make use of the interactive features, you can install the optional dependencies:

.. tabs::

  .. tab:: JupyterLab
    .. code-block:: bash

      pip install "preliz[full,lab]"

  .. tab:: Jupyter Notebook
    .. code-block:: bash

      pip install "preliz[full,notebook]"

Using conda-forge
-----------------

.. code-block:: bash

    conda install -c conda-forge preliz


Development version
-------------------

The latest development version can be installed from the main branch using pip:

.. code-block:: bash

  pip install git+https://github.com/arviz-devs/preliz.git


Contributing
============
We welcome contributions from interested individuals or groups! For information about contributing to PreliZ check out our instructions, policies, and guidelines `here <https://github.com/arviz-devs/preliz/blob/main/CONTRIBUTING.md>`_.

See the `GitHub contributor page <https://github.com/arviz-devs/preliz/graphs/contributors>`_.


Citation
========

If you find PreliZ useful in your work we kindly request that you cite the following paper:

::

  @article{Icazatti_2023,
  author = {Icazatti, Alejandro and Abril-Pla, Oriol and Klami, Arto and Martin, Osvaldo A},
  doi = {10.21105/joss.05499},
  journal = {Journal of Open Source Software},
  month = sep,
  number = {89},
  pages = {5499},
  title = {{PreliZ: A tool-box for prior elicitation}},
  url = {https://joss.theoj.org/papers/10.21105/joss.05499},
  volume = {8},
  year = {2023}
  }


Donations
=========

PreliZ, as other ArviZ-devs projects, is a non-profit project under the NumFOCUS umbrella. If you want to support PreliZ financially, you can donate `here <https://numfocus.org/donate-to-arviz>`_.