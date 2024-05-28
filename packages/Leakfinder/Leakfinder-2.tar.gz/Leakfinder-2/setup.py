from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Leakfinder", 
    version="2",  
    author="Votre Nom",
    author_email="wannaajhonson@gmail.com",
    description="Subdomain Finder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jhonsonwannaa/subfinder-by-leakix", 
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11.8',
)
