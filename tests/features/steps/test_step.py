#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_step.py
@Time    :   2022/01/30 18:02:45
@Author  :   Tim Chen
@Version :   0.0.1
@Contact :   cscomicanimation@gmail.com
@License :   MIT
@Desc    :   None
"""

# here put the import lib
import logging

from behave.log_capture import capture
from behave.runner import Context
from behave import given
from typing import NoReturn


@capture
@given('Hello world')
def step_impl(context: Context) -> NoReturn:
    logging.info("I capture log to info.log")
