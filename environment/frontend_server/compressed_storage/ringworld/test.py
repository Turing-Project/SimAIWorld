import requests
import json

if __name__ == "__main__":
    data = ""
    print("*翻译开始*")
    print("------------------------------------------")
    while data != 'q':
        data = input("翻译：")
        url = "http://fanyi.youdao.com/translate"
        header = {'i': data, 'doctype': 'json'}
        response = requests.get(url, header)
        html = response.text
        page = json.loads(html)
        result = page['translateResult'][0][0]['tgt']
        print("结果：" + result)
        print("------------------------------------------")
        print("*翻译结束*")
