#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   log.py
@Time    :   2022/01/19 14:18:56
@Author  :   shengchenj
@Version :   0.0.1
@Contact :   shengchenj@isoftstone.com
@License :   MIT
@Desc    :   None
'''

# here put the import lib
import logging
import logging.config
import os

import yaml
from yaml import SafeLoader


def setup_logging(
    name: str,
    default_path: str = './config/logging.yaml',
    default_level: int = logging.INFO,
    env_key: str = 'LOG_CFG'
) -> logging.Logger:
    """
        Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            # config = yaml.safe_load(f.read())
            config = yaml.load(f.read(), Loader=SafeLoader)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return logging.getLogger(name)
