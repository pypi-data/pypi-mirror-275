## LensMC - Weak lensing shear measurement with forward modelling and MCMC sampling

LensMC is a Python package for weak lensing shear measurement specifically developed for Euclid and stage-IV weak lensing surveys.
It is based on forward modelling and fast MCMC sampling.
To acknowledge this work, please cite the following paper: [Euclid Collaboration: G. Congedo et al. (2024)](https://arxiv.org/abs/2405.00669).

Contact: <giuseppe.congedo@ed.ac.uk>

## Dependencies

LensMC is written for Python 3, please see [requirements.txt](requirements.txt).

## Install

### From the official repository (recommended)

Please use `pip`:
```
$ pip install lensmc
```
This will fetch a source distribution and build it locally. A source distribution is preferred over a pre-built binary wheel to priotise runtime performance over build execution speed.

### Via Makefile in a conda environment

Build environment and install LensMC:
```
$ make
$ make install
```

Source the environment:
```
$ source lensmc-env/bin/activate
(lensmc-env) $ 
(lensmc-env) $ python
Python 3.9.15 | packaged by conda-forge | (main, Nov 22 2022, 15:55:03) 
[GCC 10.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import lensmc
>>>
```

### Via setuptools

LensMC can also be installed into any environment with:
```
$ python setup.py install
```
Please use the `--user` option to install it in the user space, or source an environment beforehand (e.g. as in the previous section).

### From a source distribution

Assuming a LensMC environment is available, a source distribution can be made through:
```
$ make dist
```
The output tarball will be found in the `dist` directory. This can be distributed and then installed as follows:
```
$ pip install dist/lensmc*.tar.gz
```

## Tutorial

TBD

## License

GNU Lesser General Public License - Copyright (C) 2015 Giuseppe Congedo, University of Edinburgh on behalf of the Euclid Science Ground Segment
