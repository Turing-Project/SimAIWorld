import json

from django.test import TestCase

# Create your tests here.


def test():
    with open("./name.json", "r", encoding="utf-8") as f:
        js = f.read()
        names_mapping = json.loads(js)['persona_names_mapping']
        print(names_mapping)


if __name__ == "__main__":
    test()
