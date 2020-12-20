#!/usr/bin/env python
# encoding: utf-8
'''
@author: sanxun
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@file: get_zse_86.py
@time: 2020/12/20 11:29
@desc:
感谢一只不会爬的虫子：https://blog.csdn.net/weixin_40352715/article/details/107546166
'''
import codecs
import hashlib
import os

import execjs

import conf.conf_wrapper as cf


"""
cookie: d_c0="AMDQn5NpEBKPTr5oDeuR0slU6BQV57cQfDU=|1603119063"
cookie: z_c0="2|1:0|10:1608432237|4:z_c0|92:Mi4xVHBWSkFnQUFBQUFBd05DZmsya1FFaVlBQUFCZ0FsVk5iUWpNWUFBUlRfcEh1QWk4R0s2ejItS2otZE5rZ195Wkl3|d636131b39547d9396ed8036c892bfe793b21d2fc3b7e4818a399f418d73ece4"
"""

current_path = os.path.abspath(__file__)
js_files = os.path.join(os.path.abspath(os.path.dirname(current_path)), "g_encrpyt.js")
JS_CODE = codecs.open(js_files, "r", "utf-8").read()
CTX = execjs.compile(JS_CODE, cwd=rf"{cf.get_my_config('node_modules','path')}")

def get_zse_86(query_path, referer, d_c0):
    f = "+".join([get_zse_version(), query_path, referer, f"\"{d_c0}\""])
    fmd5 = hashlib.new('md5', f.encode()).hexdigest()
    encstr = get_js_sign_bridge(fmd5)
    return "1.0_" + encstr

def get_zse_version():
    return "3_2.0"

def get_js_sign_bridge(data):
    encrypt_str = CTX.call('b', data)
    return encrypt_str


def get_zst_81():
    return "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpT67tuQ7F0K6P0Eeuy-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueTh_LGUvSmQbHmBreMigL8FGL1oqFMqwgqWBwmLvU0IUxKjbS0kDp1YDVGVwOPvAxGDg3fUUo0Lhp1SMtGfULBsqoGABX_iG2MX9V020CyzCCYgDgC7GtqhDuBiDo_gqF1WgpLeUpqCBN_69VmmqV_rgx99G2Mb_pysCC9ObwykR21HGxmvqfzugSfkvOYS92Mbgo09cwMJekBOrxMuGXBYBXOu93OiqcLmJN_gJeYJ_eVQBHm6gtM_hpqQefOrbS1KrxOr6uquq3xwDo1mqc8Jbr1e8O_3wVm1TXB2r3C"

if __name__ == '__main__':
    d = get_zse_86("/api/v4/members/ch4ron/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cexcerpt%2Cis_labeled%2Clabel_info%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B*%5D.question.has_publishing_draft%2Crelationship&offset=20&limit=20&sort_by=created", "https://www.zhihu.com/people/ch4ron/answers?page=1", "AMDQn5NpEBKPTr5oDeuR0slU6BQV57cQfDU=|1603119063")
    print(d)




