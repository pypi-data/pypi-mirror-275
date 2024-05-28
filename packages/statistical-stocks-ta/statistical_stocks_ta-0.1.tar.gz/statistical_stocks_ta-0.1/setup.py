from setuptools import setup, find_packages

setup(
    name="statistical-stocks-ta",
    version="0.1",
    author="Nils Lopez",
    author_email="lopez.nils@doctopus.app",
    description="A python package for Statistical Stocks TA (computing patterns, ma, indicators) and data fetching.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nils-Lopez/statistical-stocks-ta",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "numpy",
        "ta",
        "mplfinance",
        "ccxt",
        "scikit-learn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
