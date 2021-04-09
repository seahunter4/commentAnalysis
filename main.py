#!/usr/bin/python
# -*- coding: utf-8 -*-
# 本代码仅供参考，请根据实际情况进行调整
from wx_sdk import wx_sdk
import json


def get_comment_tag(comments, params):
    bodyStr = {}
    url = 'https://aiapi.jd.com/jdai/CommentTag'
    bodyStr["text"] = comments  # body中的内容
    response = wx_sdk.wx_post_req(url, params,
                                  bodyStr=json.dumps(bodyStr, ensure_ascii=False).encode('utf-8').decode('latin1'))
    return response.text


def get_comment_sentiment(comments, params):
    bodyStr = {}
    url = 'https://aiapi.jd.com/jdai/sentiment'
    bodyStr["type"] = 1
    bodyStr["text"] = comments  # body中的内容
    response = wx_sdk.wx_post_req(url, params,
                                  bodyStr=json.dumps(bodyStr, ensure_ascii=False).encode('utf-8').decode('latin1'))
    return response.text


if __name__ == '__main__':
    params = {
        'appkey': 'ab94cc18cdffb6f41b3ac57b0a6d1a73',
        'secretkey': 'dc5a11b5647c6f961cc2517cea5bbaaa'
    }
    # print(get_comment_tag("挺不错的东东，下次还要买",params))
    res = get_comment_sentiment("挺不错的东东，下次还要买", params)
    print(json.loads(res)["result"]['sentiment'])
