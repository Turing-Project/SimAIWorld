"""
阿牛小卖部对话规则:
通过few-shot examples, 约束大模型返回的语气词和针对不同对象的文字表达修饰，比如
    - [老板您好，我想要一碗面] -> [牛，来包三鲜伊面]
    - [也许他正在家里睡觉？或许你可以去看看] -> [搁家里睡觉呢吧？]
    - etc..

指令输入格式：
<----!INPUT ONE-SHOT EXAMPLE1!---->
<----!INPUT ONE-SHOT EXAMPLE2!---->
<----!INPUT ONE-SHOT EXAMPLE3!---->
<----!INPUT ONE-SHOT EXAMPLE4!---->
"""

# todo 代码本地测试中，待补充
