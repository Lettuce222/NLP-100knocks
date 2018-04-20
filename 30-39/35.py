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

NP = []
for word in neko_list:
    if word['pos'] == '名詞':
        NP.append(word['surface'])
    else:
        if len(NP) > 1:
            print(''.join(NP))
        NP.clear()
