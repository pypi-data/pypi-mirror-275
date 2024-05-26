from setuptools import setup, find_packages

setup(
    name="ctrader-sdk",
    version="0.1.1",
    author="Nils Lopez",
    author_email="lopez.nils@doctopus.app",
    description="A Python package for interacting with the cTrader API for trading and data fetching.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nils-Lopez/ctrader-sdk",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
