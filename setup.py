from setuptools import setup

# This call to setup() does all the work
setup(
    name="consoleimage",
    version="1.0.0",
    description="Reads image formats and prints ascii colour text to console",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://repl.it/@GoodCoderBadBoy/consoleimage",
    author="GoodCoderBadBoy",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["consoleimage"],
)