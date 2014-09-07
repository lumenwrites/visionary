#!/bin/bash
# pyvenv-3.4 pip fix
pyvenv-3.4 --without-pip venv
source ./venv/bin/activate
mkdir setup
cd setup
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz
tar -vzxf setuptools-3.4.4.tar.gz
cd setuptools-3.4.4
python setup.py install
cd ..
wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz
tar -vzxf pip-1.5.6.tar.gz
cd pip-1.5.6
python setup.py install
cd ../../
deactivate
source ./venv/bin/activate

