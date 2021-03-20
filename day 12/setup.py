from setuptools import setup
from Cython.Build import cythonize

setup(
    name='day 12',
    ext_modules=cythonize("day 12/solution_1.pyx"),
    zip_safe=False,
)