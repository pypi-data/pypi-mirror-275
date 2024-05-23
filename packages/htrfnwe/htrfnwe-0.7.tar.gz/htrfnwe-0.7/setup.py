# setup.py

import numpy as np
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(name="htrfnwe.HTC_v4", sources=["htrfnwe/HTC_v4.pyx"], include_dirs=[np.get_include()]),
    Extension(name="htrfnwe.NWE_v5", sources=["htrfnwe/NWE_v5.pyx"], include_dirs=[np.get_include()]),
    Extension(name="htrfnwe.VS_v4", sources=["htrfnwe/VS_v4.pyx"], include_dirs=[np.get_include()]),
]

# Cython compiler directives
compiler_directives = {
    'language_level': "3",
    'boundscheck': False,
    'wraparound': False,
    'initializedcheck': False,
    'cdivision': True,
    'always_allow_keywords': False,
    'unraisable_tracebacks': False,
    'binding': False
}

setup(
    include_dirs=[np.get_include()],
    name="htrfnwe",
    version="0.7",
    description="A package with multiple Cython programs for technical analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Litesh",
    author_email="liteshi55@gmail.com",
    url="https://github.com/Liteshi55/htrfnwe",
    packages=["htrfnwe"],
    setup_requires=['numpy', 'scikit-learn', 'Cython', 'setuptools'],
    install_requires=['numpy', 'scikit-learn', 'Cython'],
    ext_modules=cythonize(extensions, compiler_directives=compiler_directives, annotate=True),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Cython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)