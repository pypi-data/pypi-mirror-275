import setuptools
from pathlib import Path

setuptools.setup(               # 3 essential arguments
    name="dariopdf",
    version=1.1,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])  # tell what packages are going to be distributed
)

"""(where: StrPath = ".", exclude: Iterable[str] = (), include: Iterable[str] = ("*", )) -> list[str]"""
""" excluded tests and data from distribution"""

