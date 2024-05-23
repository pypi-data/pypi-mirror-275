from setuptools import find_packages, setup
import os

def read(fname):
    """
    Utility function to read the README file. Used for the long_description.
    :param fname:
    :return:
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

_REQUIRED = ['networkx','tqdm','petdatasetreader','matplotlib','mplcursors','pygraphviz']
_EXTRAS = []

setup(
    name='petannotationvisualizer',
    version='1.2.1',
    packages=find_packages(exclude=("tests", "docs", "dist", "build")),
    install_requires=_REQUIRED,
    # extras_require=_EXTRAS,
    package_data={'': ['*.json', '*.png', ]},
    include_package_data=True,
    platforms="Any",

    # python_requires='!=2.7, >=3.5.*',
    classifiers=[

            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",

            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: Information Technology",

            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",

            "Topic :: Scientific/Engineering",
            "Topic :: Utilities",
        ],

    author='Patrizio Bellan',
    author_email='patrizio.bellan@gmail.com',
    maintainer="Patrizio Bellan",
    maintainer_email="patrizio.bellan@gmail.com",

    url='https://pdi.fbk.eu/pet-dataset',

    license='MIT',
    keywords=["PET visualizer", "huggingface", "PET", "dataset", "process extraction from text",
              "natural language processing", "nlp", "business process management", "bpm"],
    description='A visualization tool for the PET dataset hosted on Huggingface.',
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
)
