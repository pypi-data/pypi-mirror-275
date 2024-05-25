import setuptools
import demo

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name = "danieldemo",
    version = demo.__version__,
    author="Daniel",
    description = "Simple demo package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://google.com",
    packages=setuptools.find_packages(),
    python_requires = ">=3.10"
)