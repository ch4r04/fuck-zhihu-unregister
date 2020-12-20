#!/usr/bin/env python
# encoding: utf-8
'''
@author: sanxun
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@file: del_allcollections.py
@time: 2020/12/20 16:35
@desc:
'''
import requests

import conf.conf_wrapper as cf
import request.zhihu_request as z_req
import request.gen as gen
import encrypt.get_zse_86 as zse
from bs4 import BeautifulSoup


def query_all_my_collections_id():
    page = 0
    user_name = cf.get_my_config("Cookies", "user_name")
    my_col_list = []
    col_url = f"https://www.zhihu.com/people/{user_name}/collections"
    headers = gen.gen_header(f"/people/{user_name}/collections", "")
    r = requests.get(col_url, params=None, headers=headers)
    # print(r.text)
    # todo: 正则获取id



if __name__ == '__main__':
    pins_list = query_all_my_collections_id()