import pathlib
import setuptools

setuptools.setup(
    name="Scrapelytix",
    version="0.0.2",
    description="A package to allow analyzing soccer event data easily",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Soham Basu, Debrup Mitra",
    author_email="basusoham034@gmail.com, 30debrup@gmail.com",
    license="Unlicensed",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=['python', 'soccer', 'soccer analysis', 'passing network'],
    python_requires=">=3.8,<=3.12.1",
    packages=setuptools.find_packages(),
    include_package_data=True
)
