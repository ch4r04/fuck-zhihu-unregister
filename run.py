#!/usr/bin/env python
# encoding: utf-8
'''
@author: sanxun
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@file: run.py
@time: 2020/12/20 17:19
@desc:
'''
import del_allans as dl_ans
import del_allpins as dl_pins

if __name__ == '__main__':
    id_list = dl_ans.query_all_my_answer_id()
    dl_ans.delete_all_myanswer(id_list)
    print("[*]删除所有回答成功 ")

    pins_list = dl_pins.query_all_my_pins_id()
    dl_pins.delete_all_pins(pins_list)
    print("[*]删除想法成功: ")

