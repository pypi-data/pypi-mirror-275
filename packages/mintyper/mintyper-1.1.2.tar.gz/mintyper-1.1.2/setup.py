from setuptools import setup, find_packages
from pathlib import Path
import os
import sys

# Ensure the path to version.py is correctly handled
sys.path = [os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')] + sys.path

from mintyper.version import __version__

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='mintyper',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/MBHallgren/mintyper',
    license='MIT',  # Add the appropriate license
    install_requires=[
        # List your dependencies here, e.g., 'numpy', 'pandas'
    ],
    author='Malte B. Hallgren',
    author_email='malhal@food.dtu.dk',
    description='mintyper: an outbreak-detection method for accurate and rapid SNP typing of clonal clusters with noisy long reads.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    scripts=['bin/mintyper'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version if needed
)
