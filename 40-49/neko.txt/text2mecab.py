# coding: utf-8

import MeCab
import codecs

fin = open('neko.txt', 'r')
fout = codecs.open('neko.txt.mecab', 'w')

texts = fin.readlines()
m = MeCab.Tagger()

for line in texts:
    s = m.parse(line)
    fout.write(s)