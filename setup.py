import setuptoopls

with open("README.md", "r") as fh:
    long_description = fh.read();

setuptools.setup(
    name="autoapache-jls47",
    version="0.0.1",
    author="jls47",
    author_email="jls47@u.washington.edu",
    description="Automating apache setup and configuration in servers of different operating systems",
    url="https://github.com/jls47/autoapache",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)