from setuptools import setup, find_packages

setup(
    name="swahili_stopwords",
    version="0.1.0",
    description="A library for Swahili stopwords",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alfredkondoro/swahili_stopwords", 
    author="Alfred Malengo Kondoro",
    author_email="alfredkondoro97@gmail.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
