import MeCab
import re

fin = open('neko.txt.mecab', 'r')

neko_list = []

for word in fin:
    m = re.search(r"(.*)\t(.*)", word)

    neko_dict = {}

    if m:
        neko_dict['surface'] = m.group(1)
        neko_dict['base'] = m.group(2).split(',')[6]
        neko_dict['pos'] = m.group(2).split(',')[0]
        neko_dict['pos1'] = m.group(2).split(',')[1]

    if len(neko_dict) != 0:
        neko_list.append(neko_dict)

for i in range(len(neko_list)-2):
    if neko_list[i]['pos'] == '名詞' and neko_list[i+2]['pos'] == '名詞' and neko_list[i+1]['surface'] == 'の':
        print(neko_list[i]['surface'] + neko_list[i+1]['surface'] + neko_list[i+2]['surface'])
