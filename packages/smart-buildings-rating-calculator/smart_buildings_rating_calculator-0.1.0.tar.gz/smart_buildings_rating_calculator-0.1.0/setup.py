from setuptools import setup, find_packages

setup(
    name="smart-buildings-rating-calculator",
    version="0.1.0",
    author="CentreForNetZero",
    author_email="data@centrefornetzero.org",
    description="The calculation to generate a smart building rating",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/centrefornetzero/smart-building-rating-calculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)