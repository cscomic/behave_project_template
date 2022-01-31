#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   environment.py
@Time    :   2022/01/30 17:59:01
@Author  :   Tim Chen
@Version :   0.0.1
@Contact :   cscomicanimation@gmail.com
@License :   MIT
@Desc    :   None
"""

# here put the import lib
from typing import NoReturn
from behave.log_capture import capture

from behave.runner import Context


def before_all(context: Context) -> NoReturn:
    """

    """
    # context.config.setup_logging(configfile="behave_logging.ini")
    pass


@capture
def after_all(context: Context) -> NoReturn:
    pass
