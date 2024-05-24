from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as rdme:
    setup(
        name="yaclogger",
        version="1.0.0",
        author="Wagner Cotta",
        description="".join(
            [
                "Yet Another Colorful Logger is just another logging utility ",
                "that adds color to your console log messages. ",
                "This module is already configured, not requiring any setup. ",
                "Simply install it and integrate into your Python projects. ",
                "However, if you want to customize it, you can do it as well.",
            ]
        ),
        url="https://github.com/wagner-cotta/yaclogger",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires=["colorlog"],
        license="GNU",
        long_description=rdme.read(),
        long_description_content_type="text/markdown",
    )
