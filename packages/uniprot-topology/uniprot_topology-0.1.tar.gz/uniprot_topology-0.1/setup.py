from setuptools import setup, find_packages

setup(
    name="uniprot_topology",
    version="0.1",
    packages=find_packages(),
    description="Simple parser for UniProt topological domains and other features",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Noel Garber",
    author_email="ngarber93@gmail.com",
    url="https://github.com/noelgarber/uniparser",
    install_requires=[
        "xmltodict"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)