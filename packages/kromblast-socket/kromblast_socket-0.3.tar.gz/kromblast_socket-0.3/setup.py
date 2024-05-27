from setuptools import setup
from pathlib import Path

setup(
    name="kromblast-socket",
    version="0.3",
    description="Connect to a Kromblast socket server",
    long_description=Path(__file__).parent.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/alex-bouget/KromblastSocketPy",
    author="alex-bouget",
    packages=["kb_socket"],
    install_requires=[
        "promise==2.3.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
    ]
)