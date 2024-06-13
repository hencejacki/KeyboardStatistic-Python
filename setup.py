from setuptools import setup, find_packages

setup(
    name="ks",
    version="0.0.1",
    description="A tiny tool that record your use behavior of keyboard.",
    author="hencejacki",
    author_email="hencejacki@gmail.com",
    url="https://github.com/hencejacki/KeyboardStatistic",
    packages=find_packages(exclude=["tests", "docs"]),
)
