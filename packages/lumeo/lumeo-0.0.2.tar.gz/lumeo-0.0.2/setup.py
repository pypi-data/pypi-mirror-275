from setuptools import setup, find_packages
from lumeo import __version__

setup(
    name='lumeo',
    version=__version__,
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # Add your dependencies here
    ],
)