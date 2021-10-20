from setuptools import setup, find_packages

name = "SciViz"
version = '0.0.1'

setup(
    name=name,
    version=version,
    packages=find_packages(),
    install_requires=["numpy",
                      "matplotlib",
                      "jupyter"
                      ]
)
