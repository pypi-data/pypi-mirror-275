import sys

import setuptools

sys.path.insert(0, "src")
import setter

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="setter",
    version=setter.__version__,
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
