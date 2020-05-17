from setuptools import setup, find_packages

with open('README.md','r') as readme_file:
    long_description: str = readme_file.read()

setup(
    name="python-dependency-injection",
    version="0.8",
    author="Eli Malka",
    author_email="eli.malka.mail@gmail.com",
    description="Python-dependency-injection is a simple yet powerful mini-framework for dependency injection in Python",
    license="MIT",
    keywords="python dependency injection",
    url="https://github.com/emalka/python-dependency-injection",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ],
    install_requiers=[]
)