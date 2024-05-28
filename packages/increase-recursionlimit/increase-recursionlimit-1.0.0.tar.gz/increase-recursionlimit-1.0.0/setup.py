import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="increase-recursionlimit",
    version="1.0.0",
    author="Kavi Gupta",
    author_email="kavig+increase_recursionlimit@mit.edu",
    description="Context manager to increase a recursionlimit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kavigupta/increase-recursionlimit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
)
