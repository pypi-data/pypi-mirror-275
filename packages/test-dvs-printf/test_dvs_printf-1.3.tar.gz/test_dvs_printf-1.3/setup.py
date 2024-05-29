import pathlib, setuptools

setuptools.setup(
    name="test_dvs_printf",
    version="1.3",
    description=
"Animated Visual appearance for console-based applications, with different animation styles",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/dhruvan-vyas/dvs_printf",
    author="dhruvan_vyas",
    license="MIT License",
    project_urls={
        "Documentation":"https://github.com/dhruvan-vyas/dvs_printf/blob/main/README.md",
        "hii":"https://pypi.org/project/dvs-printf",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
        "Environment :: Console"],
    python_requires=">=3.10",
    packages=setuptools.find_packages(),
    include_package_data=True,
)
