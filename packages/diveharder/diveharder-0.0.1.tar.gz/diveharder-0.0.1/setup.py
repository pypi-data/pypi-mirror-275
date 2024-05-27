from setuptools import setup, find_packages

setup(
    name="diveharder",
    version="0.0.1",
    author="AJXD2",
    author_email="aj@ajxd2.dev",
    description="Placeholder package for future development",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
