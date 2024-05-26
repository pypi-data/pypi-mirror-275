import re

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup

with open("d2cd/__init__.py", "r", encoding="utf-8") as file:
    REGEX_VERSION = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(REGEX_VERSION, file.read(), re.MULTILINE).group(1)

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

setup(
    name="d2cd",
    version=version,
    packages=find_packages(),
    description="Docker Compose Continuous Delivery",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="veerendra2",
    author_email="veerendra2@github.com",
    url="https://github.com/veerendra2/d2cd",
    download_url=f"https://github.com/veerendra2/d2cd/archive/{version}.tar.gz",
    project_urls={
        "Changelog": "https://github.com/veerendra2/d2cd/blob/master/CHANGELOG.md",
        "Documentation": "https://d2cd.readthedocs.io/en/latest/",
    },
    keywords=["gitops", "cicd", "docker-compose", "continuous delivery"],
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Utilities",
    ],
    install_requires=[
        "GitPython==3.1.43",
        "loguru==0.7.2",
        "marshmallow==3.21.1",
        "python-on-whales==0.71.0",
        "giturlparse==0.12.0",
        "yamllint==1.33.0",
    ],
    python_requires=">=3.9",
    entry_points={"console_scripts": ["d2cd = d2cd.main:main"]},
)
