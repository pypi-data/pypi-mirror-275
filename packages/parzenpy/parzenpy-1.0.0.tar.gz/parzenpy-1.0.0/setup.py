"""A module which goes through the setup of files"""
from setuptools import setup, find_packages

with open("README.md", encoding="utf8") as f:
    long_description = f.read()

setup(
    name='parzenpy',
    version='1.0.0',
    description='A package for applying smoothing to frequency spectra',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fjornelas/parzenpy',
    author='Francisco Javier Ornelas',
    author_email='jornela1@g.ucla.edu',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='parzen spectral smoothing ',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=['numpy'],
    project_urls={
        'Bug Reports': 'https://github.com/fjornelas/parzenpy/issues',
        'Source': 'https://github.com/fjornelas/parzenpy',
    },
)