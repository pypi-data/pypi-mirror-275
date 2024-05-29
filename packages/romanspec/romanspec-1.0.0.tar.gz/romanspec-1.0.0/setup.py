import os
import sys
import shutil
from setuptools import setup, find_packages, find_namespace_packages
from setuptools.command.install import install

setup(name='romanspec',
      version='1.0.1',
      description='Spectroscopy with the Roman Space Telescope',
      author='David Nidever',
      author_email='dnidever@montana.edu',
      url='https://github.com/dnidever/romanspec',
      #scripts=['bin/roman'],
      requires=['numpy','astropy(>=4.0)','scipy','dlnpyutils','thedoppler','torch','theborg'],
      zip_safe = False,
      include_package_data=True,
      packages=find_namespace_packages(where="python"),
      package_dir={"": "python"}      
)
