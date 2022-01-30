#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_step.py
@Time    :   2022/01/30 18:02:45
@Author  :   Tim Chen
@Version :   0.0.1
@Contact :   cscomicanimation@gmail.com
@License :   MIT
@Desc    :   None
'''

# here put the import lib
from behave.runner import Context
from behave import *
from typing import NoReturn

@given('Hello world')
def step_impl(context: Context) -> NoReturn:
    print("Hello World!\n\n")