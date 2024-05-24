from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

requirements = """
colorama
termcolor
sympy
coloredlogs
""".splitlines()

setup(
    name="boringcalculator",
    version="1.0.1",
    author="Dariel Fierro",
    author_email="eldarielmario@gmail.com",
    license="Copyright © 2023 Boring Calculator - All rights reserved.",
    url="https://boringcalculator.com",
    # uncomment to build source distribution
    packages=find_packages(),
    # the purpose of cythonizing is to protect the source code
    ext_modules=cythonize("boringcalculator/**/*.py"),
    install_requires=[requirements],
    python_requires=">=3.8, <3.12",
    entry_points={
        "console_scripts": ["calculate = boringcalculator.commands.__main__:main"]
    },
)
