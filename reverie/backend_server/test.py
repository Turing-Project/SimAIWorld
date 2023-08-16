"""
Author: Turing's Cat (joonspk@stanford.edu)

File: gpt_structure.py
Description: Wrapper functions for calling OpenAI APIs.

TODO:
    1.展示页面大小
    2.展示界面汉化
        - 人物状态汉化
        - 人物名称汉化
        - 系统状态汉化
    3.Django前端转发
"""
import json
import os
import random
import openai
import time

from utils import *

openai.api_key = ""
