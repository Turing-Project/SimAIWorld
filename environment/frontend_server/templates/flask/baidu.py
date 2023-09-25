
import urllib.request
import urllib.parse
import json
import requests  # pip intasll requests
import execjs  # 安装指令：pip install PyExecJS
import random
import hashlib
import re


# 百度翻译方法
def baidu_translate(content):
    print(content)
    if len(content) > 4891:
        return '输入请不要超过4891个字符！'
    salt = str(random.randint(0, 50))
    # 申请网站 http://api.fanyi.baidu.com/api/trans
    appid = '201912XXXXXXXXXXX'  # 这里写你自己申请的
    secretKey = 'e83BXpQXXXXXXXXXXX'  # 这里写你自己申请的
    sign = appid + content + salt + secretKey
    sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
    head = {'q': f'{content}',
            'from': 'en',
            'to': 'zh',
            'appid': f'{appid}',
            'salt': f'{salt}',
            'sign': f'{sign}'}
    j = requests.get('http://api.fanyi.baidu.com/api/trans/vip/translate', head)
    print(j.json())
    res = j.json()['trans_result'][0]['dst']
    res = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]').sub(' ', res)
    print(res)
    return res


if __name__ == '__main__':
    ret = baidu_translate("红色，沙发")

