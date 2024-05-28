from setuptools import find_namespace_packages, setup

setup(
    name="cerebrumscanner_hello",
    version="0.0.1.b10",
    package_dir={"": "src"},  # Specify source code directory
    packages=find_namespace_packages(where="src"),
    install_requires=[],
)
