from setuptools import setup, find_packages

setup(
    name="LLIC",
    version="0.1.0",
    author="Dan Jacobellis",
    author_email="danjacobellis@utexas.edu",
    description="A lightweight learned image codec",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danjacobellis/LLIC",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "torch",
        "compressai",
        "numpy",
    ],
)
