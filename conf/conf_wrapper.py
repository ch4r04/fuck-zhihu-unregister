#!/usr/bin/env python
# encoding: utf-8
'''
@author: sanxun
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@file: conf_wrapper.py
@time: 2020/12/20 14:41
@desc:
'''
import configparser
import os

cf = configparser.ConfigParser()
current_path = os.path.abspath(__file__)
config_file_path = os.path.join(os.path.abspath(os.path.dirname(current_path)), "conf.ini")
cf.read(config_file_path)

def get_my_config(section, keys):
    return cf.get(section, keys)

if __name__ == '__main__':
    pass
