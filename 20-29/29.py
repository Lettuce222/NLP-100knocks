#!/usr/bin/env python
#coding:utf-8
import json
import re
import urllib.parse, urllib.request

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
dictionary = {}

for line in text:
    if ' = ' in line:
        info = line.split(' = ')
        dictionary[re.sub('\|', '', info[0])] = info[1]

# 以下カンニング

fname_flag = dictionary['国旗画像']

# リクエスト生成
url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(fname_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

# MediaWikiのサービスへリクエスト送信
request = urllib.request.Request(url,
    headers={'User-Agent': 'NLP100_Python(@segavvy)'})
connection = urllib.request.urlopen(request)

# jsonとして受信
data = json.loads(connection.read().decode())

# URL取り出し
url = data['query']['pages']['-1']['imageinfo'][0]['url']
print(url)