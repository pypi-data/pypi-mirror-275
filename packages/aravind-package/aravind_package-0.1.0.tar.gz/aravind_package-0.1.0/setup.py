from setuptools import setup, find_packages

setup(
    name="aravind_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Aravind Satyanarayanan",
    author_email="aravind.bedean@gmail.com",
    description="A simple package for string utilities",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AravindSatyan/python-package.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
