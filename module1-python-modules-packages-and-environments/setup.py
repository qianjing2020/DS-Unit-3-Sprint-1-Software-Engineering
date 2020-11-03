# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-pkg-qianjing2020",  # the name that you will install via pip
    version="1.0",
    author="Jing Qian",
    author_email="jjqian@gmail.com",
    description="A short demo for package distribution",
    long_description=long_description,
    # required if using a md file for long desc
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/qianjing2020/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module1-python-modules-packages-and-environments",
    #keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
