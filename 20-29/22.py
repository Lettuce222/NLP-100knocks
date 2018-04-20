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
        text = dictionary[k1]["text"].split('\n')
        break

for line in text:
    if "Category" in line:
        temp_cate_val = line.split(":")
        print(re.sub(r'[\]\*\|]',"",temp_cate_val[1]))