"""
    Setup file for behave_project_template.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.1.4.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import pathlib

from setuptools import setup
from pkg_resources import parse_requirements

with pathlib.Path('docs/requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in parse_requirements(requirements_txt)
    ]

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="behave_project_template",
    install_requires=install_requires
)
