
from translate import Translator


def local_trans(src_token, src='en', dest='zh'):
    translator = Translator(from_lang=src, to_lang=dest)
    result = translator.translate(src_token)
    return result  # 打印翻译结果


if __name__ == '__main__':
    res = local_trans("How are you enjoying your meal? I wanted to let you know that I'm planning a Valentine's Day "
                      "party at Hobbs Cafe on February 14th, 2023 from 5pm to 7pm. I would love for you to join us!")
    print(f"""target sentence: {res}""")
