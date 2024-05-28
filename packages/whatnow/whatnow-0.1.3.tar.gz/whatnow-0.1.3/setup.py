from setuptools import setup, find_packages

setup(
    name="whatnow",
    version="0.1.3",
    author="Deepak Kumar Upadhayay",
    author_email="dku3132@gmail.com",
    description="A module to get the the current Day, Date, Time and Temperature",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/inspironman/whatnow",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
