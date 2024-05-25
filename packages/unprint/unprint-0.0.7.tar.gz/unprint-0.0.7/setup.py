from time import time
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unprint",
    version="0.0.6",
    author="Liu Zuo Lin",
    author_email="zlliu246@gmail.com",
    description="A simple package to unprint lines in the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)