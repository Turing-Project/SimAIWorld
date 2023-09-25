import urllib.request
import urllib.parse
import json
import requests  # pip intasll requests
import execjs  # 安装指令：pip install PyExecJS
import random
import hashlib
import re


# 有道翻译方法，不支持一次翻译一大段文字
def youdao_translate(content):
    '''实现有道翻译的接口'''
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
    data = {
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1500092479607',
        'sign': 'd9f9a3aa0a7b34241b3fe30505e5d436',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CL1CKBUTTON',
        'typoResult': 'true'}
    data['i'] = content.replace('\n', '')
    data = urllib.parse.urlencode(data).encode('utf-8')
    wy = urllib.request.urlopen(url, data)
    html = wy.read().decode('utf-8')
    ta = json.loads(html)
    res = ta['translateResult'][0][0]['tgt']
    return res


if __name__ == '__main__':
    res = youdao_translate("红色，沙发")