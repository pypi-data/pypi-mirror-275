from setuptools import setup, find_packages

setup(
    name="diamond-hpc",
    version="0.0.1",
    author="Haotian XIE, Gengcong YANG",
    author_email="hotinexie@gmail.com",
    description="Diamond is a Python package for running tasks on HPC.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Diamond-Proj/Diamond",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
