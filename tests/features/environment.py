#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   environment.py
@Time    :   2022/01/30 17:59:01
@Author  :   Tim Chen
@Version :   0.0.1
@Contact :   cscomicanimation@gmail.com
@License :   MIT
@Desc    :   All behave running hook functions, sort by running sequence
"""

# here put the import lib
from typing import NoReturn
from behave.model import Tag, Feature, Scenario, Step
from behave.runner import Context


def before_all(context: Context) -> NoReturn:
    """Running before the whole shooting match.

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.

    Returns:

    """
    # TODO: Using yaml format configure file instead of ini file
    context.config.setup_logging(configfile="tests/config/logging.ini")
    pass


def before_tag(context: Context,
               tag: Tag) -> NoReturn:
    """Running before a section tagged with the given name.

    They are invoked for each tag encountered in the order they’re found in the feature file.
    See Controlling Things With Tags.
    The tag passed in is an instance of Tag and because it’s a subclass of string you can do simple tests like:
        if tag.startswith("browser."):
            pass

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.
        tag (behave.model.Tag): special tags with features

    Returns:

    """
    pass


def before_feature(context: Context,
                   feature: Feature) -> NoReturn:
    """Running before each feature file is exercised. The feature passed in is an instance of Feature.

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.
        feature (behave.model.Feature): features

    Returns:

    """
    pass


def before_scenario(context: Context,
                    scenario: Scenario) -> NoReturn:
    """Running before each scenario is run. The scenario passed in is an instance of Scenario.

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.
        scenario (behave.model.Scenario): scenarios

    Returns:

    """
    pass


def before_step(context: Context,
                step: Step) -> NoReturn:
    """Running before every step. The step passed in is an instance of Step.

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.
        step (behave.model.Step): steps

    Returns:

    """
    pass


def after_step(context: Context,
               step: Step) -> NoReturn:
    """Running after every step. The step passed in is an instance of Step.

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.
        step (behave.model.Step): steps

    Returns:

    """
    pass


def after_scenario(context: Context,
                   scenario: Scenario) -> NoReturn:
    """Running after each scenario is run. The scenario passed in is an instance of Scenario.

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.
        scenario (behave.model.Scenario): scenarios

    Returns:

    """
    pass


def after_feature(context: Context,
                  feature: Feature) -> NoReturn:
    """Running after each feature file is exercised. The feature passed in is an instance of Feature.

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.
        feature (behave.model.Feature): features

    Returns:

    """
    pass


def after_tag(context: Context,
              tag: Tag) -> NoReturn:
    """Running after a section tagged with the given name.

    They are invoked for each tag encountered in the order they’re found in the feature file.
    See Controlling Things With Tags.
    The tag passed in is an instance of Tag and because it’s a subclass of string you can do simple tests like:
        if tag.startswith("browser."):
            pass

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.
        tag (behave.model.Tag): special tags with features
    Returns:

    """
    pass


def after_all(context: Context) -> NoReturn:
    """Running after the whole shooting match.

    Args:
        context (behave.runner.Context): used by behave framework, store with scenario, feature, user data and so on.

    Returns:

    """
    pass
