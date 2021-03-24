from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name='day 18',
    ext_modules=cythonize("day 18/solution_1.pyx"),
    zip_safe=False,
    include_dirs=[numpy.get_include()]
)

# python3 setup.py build_ext --inplace