from setuptools import setup, find_packages

VERSION = '0.0.8'
DESCRIPTION = "opa_oz's python utils"
LONG_DESCRIPTION = "Python package with stuff that I'm interested in"

setup(
    name="opyls",
    version=VERSION,
    author="Vladimir Levin",
    author_email="opaozhub@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'utils'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
