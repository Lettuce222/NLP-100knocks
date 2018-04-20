#!/usr/bin/env python
#coding:utf-8
import json

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
        print(line)