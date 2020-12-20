#!/usr/bin/env python
# encoding: utf-8
'''
@author: sanxun
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@file: del_allpins.py
@time: 2020/12/20 16:27
@desc:
'''
import conf.conf_wrapper as cf
import request.zhihu_request as z_req
import request.gen as gen
import encrypt.get_zse_86 as zse


def query_all_my_pins_id():
    page = 0
    user_name = cf.get_my_config("Cookies", "user_name")
    host = "https://www.zhihu.com"
    my_pins_id_list = []
    while True:
        offset = page * 20
        query_path = f"/api/v4/members/{user_name}/pins"
        referer = f"https://www.zhihu.com/people/{user_name}/pins?page={page}"
        query_param = f"offset={offset}&limit=20&includes=data%5B*%5D.upvoted_followees%2Cadmin_closed_comment"
        # abs_url = host + query_path + "?" + query_param
        headers = gen.gen_header(query_path + "?" + query_param, referer)
        r = z_req.get(host + query_path, params=query_param, headers=headers)
        for ans_items in r['data']:
            my_pins_id_list.append(ans_items['id'])
        if r['paging']['is_end']:
            break
        page = page + 1
    return my_pins_id_list

def delete_all_pins(pins_id_list):
    user_name = cf.get_my_config("Cookies", "user_name")
    host = "https://www.zhihu.com"
    referer = f"https://www.zhihu.com/people/{user_name}/pins"
    for id in pins_id_list:
        query_path = f"/api/v4/pins/{id}"
        headers = gen.gen_header(query_path, referer=referer)
        headers['x-zst-81'] = zse.get_zst_81()
        z_req.delete(host + query_path, headers=headers)
        print("[*]删除想法成功: ", str(id))



if __name__ == '__main__':
    pins_list = query_all_my_pins_id()
    delete_all_pins(pins_list)
    print("[*]删除想法成功: ")