#!/usr/bin/env python
# encoding: utf-8
'''
@author: sanxun
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@file: gen.py
@time: 2020/12/20 14:28
@desc:
'''
import os

import encrypt.get_zse_86
import conf.conf_wrapper as cf


def gen_header(path, referer):
    z_c0 = cf.get_my_config("Cookies", 'z_c0')
    d_c0 = cf.get_my_config("Cookies", 'd_c0')
    encrypt_str = encrypt.get_zse_86.get_zse_86(path, referer, d_c0)
    headers = {
        "referer": referer,
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "cookie": f'd_c0="{d_c0}"; z_c0="{z_c0}"',
        "x-zse-83": "3_2.0",
        "x-zse-86": encrypt_str,
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7"
    }
    return headers

if __name__ == '__main__':
    head = gen_header("/api/v4/members/ch4ron/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cexcerpt%2Cis_labeled%2Clabel_info%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B*%5D.question.has_publishing_draft%2Crelationship&offset=20&limit=20&sort_by=created",
                      "https://www.zhihu.com/people/ch4ron/answers?page=1")
    print(head)