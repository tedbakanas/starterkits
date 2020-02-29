from setuptools import setup
from swiptapi.__version__ import __version__
import os

top_level_dir = os.path.dirname((os.getcwd()))
with open(os.path.join(top_level_dir,"README.md"), "r") as fh:
    long_description = fh.read()
with open(os.path.join(top_level_dir,"LICENSE"), "r") as lc:
    license = lc.read()

setup(
    name="swiptapi",
    version=__version__,
    description="A simple package for hitting the open Swiss Public Transit API.",
    url="https://github.com/tedbakanas/starterkits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Theodore Bakanas",
    author_email="tedbakanas@gmail.com",
    license=license,
    packages=["swiptapi"],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires='>=3'
)