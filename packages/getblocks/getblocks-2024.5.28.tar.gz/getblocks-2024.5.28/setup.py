from setuptools import setup

from getblocks import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "getblocks",
    version = __version__,
    description = "Down to the smallest sector detail!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/4n6ir/getblocks",
    author = "John Lukach",
    author_email = "hello@4n6ir.com",
    license = "Apache-2.0",
    packages = [
        "getblocks"
    ],
    install_requires = [
        "blake3",
        "requests"
    ],
    zip_safe = False,
    entry_points = {
        "console_scripts": [
            "getblocks=getblocks.cli:main"
        ],
    },
    python_requires = ">=3.8",
)
