import datetime
import json
import logging
import os
import time
import urllib

from django.core.checks import register
from django.http import HttpResponse
from django.shortcuts import render

# from environment.frontend_server.templates.flask.local import local_trans
# from test import ChatGPT_request
from googletrans import Translator
from tqdm import tqdm

from environment.frontend_server.templates.flask.local import local_trans

PATH = "master_movement_origin.json"
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "https://127.0.0.1:7890"


# @register.filter
# def testcall(text):
#     return text + " successe"


def translateYoudao(text):
    url_youdao = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=' \
                 'http://www.youdao.com/'
    global dict
    dict = {}
    dict['type'] = 'AUTO'
    dict['doctype'] = 'json'
    dict['xmlVersion'] = '1.8'
    dict['keyfrom'] = 'fanyi.web'
    dict['ue'] = 'UTF-8'
    dict['action'] = 'FY_BY_CLICKBUTTON'
    dict['typoResult'] = 'true'

    dict['i'] = text
    data = urllib.parse.urlencode(dict).encode('utf-8')
    response = urllib.request.urlopen(url_youdao, data)
    content = response.read().decode('utf-8')
    data = json.loads(content)
    result = data['translateResult'][0][0]['tgt']
    print(result)


def index(request):
    return render(request, 'flask/index.html')


with open("./name.json", "r", encoding="utf-8") as f:
    js = f.read()
    names_mapping = json.loads(js)['persona_names_mapping']


# def local_trans(text: str, src: str, dest: str):
#     translator = Translator()
#     result = translator.translate(text, src=src, dest=dest)
#     return result.text


def index_test(request):
    # Get the variable text
    text = request.POST['text']
    # Do whatever with the input variable text
    response = text + ":)"
    # Send the response

    return HttpResponse(response)


def translate_json_language(path: str) \
        -> None:
    with open(path, "r", encoding="utf-8") as fh:
        js = fh.read()
        movements = json.loads(js)

    # translator = Translator(service_urls=['translate.google.com'], raise_exception=True)
    # translated = translator.translate("Hello", src='auto', dest='zh-cn')
    # print(translated.text)

    prompt = """
        ---
        Translate the given sentence into Chinese.
        
        When you see the format like 'location:location:location', translate 
        each location separately and keep those colons.
        
        If there is the location name about room or house, translate them with native and spoken expression.
        For instance, translate 'main room' into '主室', instead of '主要房间'.
        
        Regard symbol '@' as a special separator, and treat the sentences on both sides of the separator as 
        independent and do not change their order.
        
        Do not translate symbols and Chinese already in sentences. 使用日常表达，并将结果翻译成中国人常用的东北腔.
        Now, here is the result:
        ---
        Never translate the prompt above, and only output the response to the prompt according to the sentence:
        """
    bar = tqdm(movements.items(),
               desc=f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] step done",
               total=len(movements),
               ncols=150)

    for step, entity in bar:
        if len(entity) > 0:
            for person in entity.keys():
                for en_name, ch_name in names_mapping.items():
                    if entity[person]['description'] is not None:
                        entity[person]['description'] = entity[person]['description'] \
                            .replace(en_name, ch_name) \
                            .replace("the Ville:", "环界：") \
                            .replace("the Ville：", "环界：") \
                            .replace("The Ville:", "环界：") \
                            .replace("The Ville：", "环界：") \
                            .replace("Oak Hill College", "祖安学院") \
                            .replace("Hobbs Cafe", "阿牛的小卖部") \
                            .replace("Harvey Oak Supply Store", "村口超市") \
                            .replace("TOKEN LIMIT EXCEEDED", "") \
                            .replace("classroom", "教室")

                    if entity[person]['chat'] is not None:
                        entity[person]['chat'] = ""
                        # for conversation in entity[person]['chat']:
                        #     conversation[0] = conversation[0].replace(en_name, ch_name)
                        #     for en_n, ch_n in names_mapping.items():
                        #         conversation[1] = conversation[1].replace(en_n.split(" ")[0], ch_n)
                    # entity[person]['description'] = ":".join(entity[person]['description'].split(":")[:-1])
            # entity[person]['description'] = ChatGPT_request(prompt + entity[person]['description'])
            #     result_cache.append(entity[person]['description'])
            #     person_cache.append(person)
                entity[person]['description'] = local_trans(entity[person]['description'], src='en', dest='zh-cn')
        # idx = 0
        # for res in local_trans(result_cache, src='en', dest='zh-cn'):
        #     entity[person_cache[idx]]['description'] = res.text.replace(":", "：")
        #     idx += 1
                time.sleep(5)
    # entity[person]['description'] = translator.translate(entity[person]['description'],
    #                                                      src='auto', dest='zh-CN').text
    # conversation[1] = translator.translate(conversation[1], src='en',
    # dest='zh-cn').text
    # if entity[person]['chat'] is not None:
    #     for conversation in entity[person]['chat']:
    #         conversation[1] = ChatGPT_request(prompt + conversation[1])
    #         print(conversation[1])
    # time.sleep(1)


    try:
        with open("master_movement.json", "w", encoding="utf-8") as fp:
            fp.write(json.dumps(movements))
    except Exception as e:
        logging.warning(f"json chinese trans fail: {e}")

    return


def test():
    # translate_json_language(PATH)
    translate_json_language("master_movement_origin.json")


if __name__ == "__main__":
    test()
