"""
    Setup file for behave_project_template.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.1.4.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="behave_project_template",
    install_requires=reqs
)
