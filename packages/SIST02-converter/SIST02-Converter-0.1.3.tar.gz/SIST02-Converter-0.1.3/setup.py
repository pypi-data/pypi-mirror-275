from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")
setup(
    name="SIST02-Converter",
    version="0.1.3",
    LICENSE = 'MIT',
    description="Conversion of input URL to SIST02 style.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    CLASSIFIERS=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
    ],
)