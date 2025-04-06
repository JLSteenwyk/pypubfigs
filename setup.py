from os import path
from setuptools import setup, find_packages


version = {}
with open(path.join("pypubfigs", "version.py")) as f:
    exec(f.read(), version)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pypubfigs",
    version=version["__version__"],
    description="Colorblind-friendly color palettes and themes for publication-quality scientific figures using matplotlib and seaborn.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jacob L. Steenwyk",
    author_email="jlsteenwyk@gmail.com",
    url="https://github.com/jlsteenwyk/pypubfigs",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "seaborn>=0.12.2",
        "matplotlib>=3.7.0"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.8",
)

## push new version to pypi
# rm -rf dist
# python3 setup.py sdist bdist_wheel --universal
# twine upload dist/* -r pypi
