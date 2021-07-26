#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 上午9:20
# @Author  : lt
# 该脚本用于发送企业微信消息
import sys
import requests
import os
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    url = os.environ["DA_NAO_WX_ROBOT"]
    payload = '{"msgtype": "text","text": {"content": "您今天打卡了吗？我是来自github action 机器人","mentioned_list":["@all"],"mentioned_mobile_list":["@all"]}}'
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
