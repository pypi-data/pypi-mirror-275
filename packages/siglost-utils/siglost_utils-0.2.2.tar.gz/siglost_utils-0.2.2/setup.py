from setuptools import setup, find_packages
from siglost_utils import __version__

setup(
    name='siglost_utils',
    version=__version__,
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # Add your dependencies here
    ],
)