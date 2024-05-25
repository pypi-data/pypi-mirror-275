from setuptools import find_packages, setup

with open("pypi/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="DataHandlerForCSV",
    version="0.9.1",
    description="data cleaner",
    package_dir={"": "pypi"},
    packages=find_packages(where="pypi"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CorbeauDistingue/dataHandlerCSV/tree/main",
    author="Burak Nafi Girgin",
    author_email="bnafigrgn@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10", 
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6, <3.12',
)