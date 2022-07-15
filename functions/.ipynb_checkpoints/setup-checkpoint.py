from distutils.core import setup
from Cython.Build import  cythonize
setup(
    ext_modules=cythonize("minute_framing.pyx", compiler_directives={'language_level' : "2"})
)
