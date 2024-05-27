from setuptools import setup, find_packages

setup(
    name="cathealthpy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
    ],
    author="Aika",
    author_email="s2222093@stu.musashino-u.ac.jp",
    description="A package for tracking and analyzing cat health data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FurutaAika/cathealthpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)