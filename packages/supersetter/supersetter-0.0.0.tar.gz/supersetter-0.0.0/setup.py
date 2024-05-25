import sys

import setuptools

sys.path.insert(0, "src")
import supersetter

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="supersetter",
    version=supersetter.__version__,
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[],
    python_requires=">=3.0",
    install_requires=[],
    extras_require={},
)
