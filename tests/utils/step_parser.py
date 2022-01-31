#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   step_parser.py
@Time    :   2022/1/31 19:49
@Author  :   Tim Chen
@Version :   0.0.1
@Contact :   cscomicanimation@gmail.com
@License :   MIT
@Desc    :   Parse utils for step definitions
             For example, if we need to parse money from step: "When I sell my cell, I will get $600.00"
             we don't need to use "...get $\\d+\\.\\d{2}" everytime
             we want "...get ${paid:Money}" for it, more easy to read,
             then we need to do two things below:
                 1. define a function, use pattern "\\d+\\.\\d{2}" to get string type of money as argument
                 2. use "register_type" binding this function as Money type
"""

# here put the import lib
from behave import register_type
import parse
from decimal import Decimal


@parse.with_pattern(r"\d+")
def parse_number(text: str) -> int:
    """

    Args:
        text (str): Number in string type

    Returns:
        (int): Number in int type

    """
    return int(text)


@parse.with_pattern(r"【[^【】]*?】")
def parse_parameter(text: str) -> str:
    """

    Args:
        text (str): Parameter in step define surround with: 【】, such as "search 【laptop】 with Google"

    Returns:
        (str): Parameter string, such as laptop

    """
    return text[1:-1]


@parse.with_pattern(r"【[^【】]*?】")
def parse_parameter_list(text: str) -> list:
    """

    Args:
        text (str): Parameter in step define surround with: 【】, such as "search 【laptop, best laptop】 with Google"

    Returns:
        (list): List of parameter, such as ["laptop", "best laptop"]

    """
    return text[1:-1].split(",")


@parse.with_pattern(r"\d+\.\d+")
def parse_money(text: str) -> Decimal:
    """

    Args:
        text (str): Money in string type

    Returns:
        (decimal): Money in decimal type, round with two decimal points

    """
    return Decimal(text).quantize(Decimal("0.00"))


register_type(Number=parse_number)
register_type(Parameter=parse_parameter)
register_type(ParameterList=parse_parameter_list)
register_type(Money=parse_money)
