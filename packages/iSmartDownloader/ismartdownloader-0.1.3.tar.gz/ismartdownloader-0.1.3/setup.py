from setuptools import setup, find_packages

setup(
    name="iSmartDownloader",
    version="0.1.3",
    description="A Python library for efficiently downloading files with support for resuming interrupted downloads.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Paisen",
    author_email="senpaikoudo@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "result>=0.6.0",
        "tqdm>=4.56.0",
        "aiohttp>=3.7.4",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.2",
            "flake8>=3.8.4",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
