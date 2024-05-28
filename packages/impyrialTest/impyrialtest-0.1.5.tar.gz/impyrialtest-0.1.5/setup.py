# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author="Ahmed Elkhodary",
    description="A package for converting imperial lengths and weights.",
    name="impyrialTest",
    packages=find_packages(include=["impyrialTest", "impyrialTest.*"]),
    install_requires=['numpy'],
    version="0.1.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)