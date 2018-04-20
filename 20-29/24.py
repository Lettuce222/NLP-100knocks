#!/usr/bin/env python
#coding:utf-8
import json
import re

f = open('jawiki-country.json', 'r')

dictionary = {}

for (i,line) in enumerate(f):
    dictionary[i] = json.loads(line)

f.close()

for k1,v1 in dictionary.items() :
    if dictionary[k1]["title"] == u"イギリス":
        text = dictionary[k1]["text"]
        break

text = text.split('\n')

for line in text:
    if 'ファイル' in line:
        print(line)
