# coding: utf-8

import re
import codecs
from matplotlib import pyplot as plt

fin = codecs.open('neko.txt.mecab', 'r', 'utf-8')

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
word_list.sort(key=lambda x:x[1], reverse=True)

rank = [i for i in range(len(word_list))]
count = [word_list[i][1] for i in range(len(word_list))]

plt.xscale("log")
plt.yscale('log')
plt.grid(which="both")

plt.plot(rank, count)
plt.show()



