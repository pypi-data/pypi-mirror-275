from setuptools import setup, find_packages

setup(
    name="getsha256",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'getsha256=getsha256:main',
        ],
    },
    install_requires=[],
    author="surendra",
    description="A simple tool to compute SHA-256 hashes for files.",
    keywords="sha256 hash file",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
