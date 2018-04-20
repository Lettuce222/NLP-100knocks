# coding: utf-8

import MeCab
import re
import numpy as np
from matplotlib import pyplot as plt

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

word_list = [a['base'] for a in neko_list]
count_list = [word_list.count(e) for e in set(word_list)]

print(count_list)

plt.hist(count_list, )
plt.show()