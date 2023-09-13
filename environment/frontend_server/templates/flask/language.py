import json
import logging
import os
import time

from django.http import HttpResponse
from django.shortcuts import render

from django.template.defaulttags import register
from googletrans import Translator

from environment.frontend_server.templates.flask.local import local_trans
from test import ChatGPT_request

PATH = "./master_movement.json"
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "https://127.0.0.1:7890"

# @register.filter
# def testcall(text):
#     return text + " successe"

with open("./name.json", "r", encoding="utf-8") as f:
    js = f.read()
    names_mapping = json.loads(js)['persona_names_mapping']


def index(request):
    return render(request, 'flask/index.html')


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
    try:
        for step, entity in movements.items():
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
                                .replace("Hobbs Cafe", "阿牛的小卖部")

                        if entity[person]['chat'] is not None:
                            for conversation in entity[person]['chat']:
                                conversation[0] = conversation[0].replace(en_name, ch_name)
                                for en_n, ch_n in names_mapping.items():
                                    conversation[1] = conversation[1].replace(en_n.split(" ")[0], ch_n)
                    # entity[person]['description'] = ChatGPT_request(prompt + entity[person]['description'])
                    entity[person]['description'] = local_trans(entity[person]['description'],
                                                                src='en', dest='zh').replace(":", "：")
                    print(entity[person]['description'])
                    # entity[person]['description'] = translator.translate(entity[person]['description'],
                    #                                                      src='auto', dest='zh-CN').text

                    # conversation[1] = translator.translate(conversation[1], src='en',
                    # dest='zh-cn').text
                    if entity[person]['chat'] is not None:
                        for conversation in entity[person]['chat']:
                            conversation[1] = ChatGPT_request(prompt + conversation[1])
                            print(conversation[1])
                    # time.sleep(1)
    except Exception as e:
        logging.warning(f"json chinese trans fail: {e}")

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(json.dumps(movements, ensure_ascii=False))

    return


def main():
    translate_json_language(PATH)


if __name__ == "__main__":
    main()
