from image_aspect import __description__
from image_aspect import __version__
from setuptools import setup
from setuptools import find_packages

setup(
    name='image_aspect',
    author='Alexandre Villela (SleX)',
    author_email='sx.slex@gmail.com',
    version=__version__,
    description=__description__,
    keywords='image_aspect library adjust image aspect',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
)
