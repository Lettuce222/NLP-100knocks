# coding: utf-8

import MeCab
import re
import numpy as np
from matplotlib import pyplot

pyplot.rcParams['font.family'] = 'IPAGothic'

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
word_list = [[e, word_list.count(e)] for e in set(word_list)]
word_list.sort(key=lambda x: x[1], reverse=True)

left = np.array([i + 1 for i in range(10)])
height = np.array([int(word_list[i][1]) for i in range(10)])
labels = np.array([word_list[i][0] for i in range(10)])

print(labels)

pyplot.bar(left, height, align="center", tick_label=labels)
pyplot.show()
