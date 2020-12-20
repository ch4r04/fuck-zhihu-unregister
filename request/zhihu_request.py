#!/usr/bin/env python
# encoding: utf-8
'''
@author: sanxun
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@file: zhihu_request.py
@time: 2020/12/20 15:13
@desc:
'''
import requests

def get(url, params,headers, **kwargs):
    r = requests.get(url, params=params, headers=headers, **kwargs)
    return r.json()

def delete(url, headers, **kwargs):
    r = requests.delete(url, headers=headers, **kwargs)
    return r.json()