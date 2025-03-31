from setuptools import setup, find_packages

setup(
    name="project-templates-cli",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        "project_templates_cli": ["templates/*", "templates/*/*", "templates/*/*/*"],
    },
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.7.0",
    ],
    entry_points={
        "console_scripts": [
            "project-templates=project_templates_cli.__main__:app",
        ],
    },
    author="Isaac Flath",
    description="A CLI tool for managing project templates",
    python_requires=">=3.7",
) 