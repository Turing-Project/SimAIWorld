
# from translate import Translator
import logging
import os

from googletrans import Translator

translator = Translator(service_urls=['translate.google.com'])

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "https://127.0.0.1:7890"
translator.raise_Exception = True


def local_trans(src_token, src='en', dest='zh-cn'):
    try:
        result = translator.translate(src_token, src=src, dest=dest)
        return result.text  # 打印翻译结果

    except Exception as e:
        logging.warning(e)

    return ""



if __name__ == '__main__':
    res = local_trans("are you enjoying your meal? I wanted to let you know that I'm planning a Valentine's Day")
    print(f"""target sentence: {res}""")
