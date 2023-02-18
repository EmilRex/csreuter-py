from setuptools import find_packages, setup

install_requires = open("requirements.txt").read().strip().split("\n")
dev_requires = open("requirements-dev.txt").read().strip().split("\n")

setup(
    # Package metadata
    name="csreuter",
    description="Python package that likes Maine a little too much.",
    author="Emil Christensen",
    author_email="emil.rex.christensen@gmail.com",
    url="https://github.com/EmilRex/csreuter-py",
    project_urls={
        "Changelog": "https://github.com/EmilRex/csreuter-py/blob/main/CHANGELOG.md",
        "Source": "https://github.com/EmilRex/csreuter-py",
        "Tracker": "https://github.com/EmilRex/csreuter-py/issues",
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # Versioning
    version="0.1.0",
    # Package setup
    packages=find_packages(include=["csreuter", "csreuter.*"]),
    include_package_data=True,
    # CLI
    entry_points={"console_scripts": ["csreuter=csreuter.cli:app"],},
    # Requirements
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
