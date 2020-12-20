#!/usr/bin/env python
# encoding: utf-8
'''
@author: sanxun
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@file: del_allans.py
@time: 2020/12/20 10:49
@desc:
'''
import codecs
import execjs

import conf.conf_wrapper as cf
import request.zhihu_request as z_req
import request.gen as gen
import encrypt.get_zse_86 as zse


def query_all_my_answer_id():
    page = 0
    user_name = cf.get_my_config("Cookies", "user_name")
    host = "https://www.zhihu.com"
    my_answer_id_list = []
    while True:
        offset = page * 20
        query_path = f"/api/v4/members/{user_name}/answers"
        referer = f"https://www.zhihu.com/people/{user_name}/answers?page={page}"
        query_param = f"include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cexcerpt%2Cis_labeled%2Clabel_info%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B*%5D.question.has_publishing_draft%2Crelationship&offset={offset}&limit=20&sort_by=created"
        # abs_url = host + query_path + "?" + query_param
        headers = gen.gen_header(query_path + "?" + query_param, referer)
        r = z_req.get(host + query_path, params=query_param, headers=headers)
        for ans_items in r['data']:
            my_answer_id_list.append(ans_items['id'])
        if r['paging']['is_end']:
            break
        page = page + 1
    return my_answer_id_list

def delete_all_myanswer(ans_id_list):
    user_name = cf.get_my_config("Cookies", "user_name")
    host = "https://www.zhihu.com"
    referer = f"https://www.zhihu.com/people/{user_name}/answers"
    for id in ans_id_list:
        query_path = f"/api/v4/answers/{id}"
        headers = gen.gen_header(query_path, referer=referer)
        headers['x-zst-81'] = zse.get_zst_81()
        z_req.delete(host + query_path, headers=headers)
        print("[*]删除回答成功: ", str(id))


if __name__ == '__main__':
    id_list = query_all_my_answer_id()
    delete_all_myanswer(id_list)
    print("[*]删除所有回答成功 ")
    pass