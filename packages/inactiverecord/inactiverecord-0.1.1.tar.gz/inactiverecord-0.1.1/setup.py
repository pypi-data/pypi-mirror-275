from setuptools import setup, find_packages

setup(
    name="inactiverecord",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Nick Schrock",
    description="Application storage framework built on eventual consistency, immutable logs, with software-defined schema and index management.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/checkrepublic",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
