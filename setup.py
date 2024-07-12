from setuptools import setup, find_packages

setup(
    name="my-project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "my-tool = src.cli:main",
        ],
    },
)