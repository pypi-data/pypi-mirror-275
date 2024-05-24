from setuptools import setup, find_packages

setup(
    name="epik8spydev",
    version="0.1.0",
    description="A package for controlling motors,camera,magnets with EPICS and asyncio.",
    packages=find_packages(),
    install_requires=[
        "pyepics",
        "asyncio"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)