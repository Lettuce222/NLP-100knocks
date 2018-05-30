# -*- coding: utf-8 -*-

import morph
from graphviz import Digraph

if __name__ == '__main__':
    fin = open("neko.txt.cabocha", "r")

    texts = morph.file2texts(fin)
    sentences = []
    [sentences.append(morph.text2chunks(text)) for text in texts]

    [chunk.print_all() for chunk in sentences[7]]

    # formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
    G = Digraph(format='png')
    G.attr('node', shape='circle')

    # ノードの追加
    for i, chunk in enumerate(sentences[7]):
        G.node(str(i), chunk.get_surface())

    #エッジの追加
    for i, chunk in enumerate(sentences[7]):
        if chunk.dst != '-1':
            G.edge(str(i), chunk.dst)

    # print()するとdot形式で出力される
    print(G)

    # binary_tree.pngで保存
    G.render('44result')