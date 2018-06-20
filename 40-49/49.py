# -*- coding: utf-8 -*-

import morph
import re
import copy
import time

if __name__ == '__main__':
    # スタート時間
    start = time.time()

    fin = open("neko.txt.cabocha", "r")

    texts = morph.file2texts(fin)
    sentences = []
    [sentences.append(morph.text2chunks(text)) for text in texts]

    fout = open('49result.txt', 'w')

    for i, sentence in enumerate(sentences):
        fout.write('{0}\n'.format(i+1))

        for chunk_id, chunk in enumerate(sentence):
            if '名詞' in [morph.pos for morph in chunk.morphs]:

                # chunkのクローンを作成
                chunk_X = copy.deepcopy(chunk)
                for morph in chunk_X.morphs:
                    if morph.pos != '助詞':
                        morph.surface = 'X'

                # Xから根へのパス
                node = chunk_X
                dst_X = []
                while (node.dst != '-1'):
                    node = sentence[int(node.dst)]
                    dst_X.append(int(node.ID))

                for chunk2 in sentence[chunk_id+1:]:
                    if '名詞' in [morph.pos for morph in chunk2.morphs]:

                        # chunk2のクローンを作成
                        chunk_Y = copy.deepcopy(chunk2)
                        for morph in chunk_Y.morphs:
                            if morph.pos != '助詞':
                                morph.surface = 'Y'

                        # Xから根までのパス中にYを含む場合
                        if int(chunk_Y.ID) in dst_X:
                            X = '{0}'.format(re.sub(r'X+', 'X', chunk_X.get_surface()))
                            fout.write('{0}({1})'.format(X, chunk.get_surface()))
                            for chunk_id2 in dst_X:
                                if int(chunk_Y.ID) == chunk_id2:
                                    break
                                fout.write(' -> {0}'.format(sentence[chunk_id2].get_surface()))
                            Y = '{0}'.format(re.sub(r'Y+', 'Y', chunk_Y.get_surface()))
                            fout.write(' -> {0}({1})\n'.format(Y, chunk2.get_surface()))
                            continue

                        # Yから根へのパス
                        node = chunk_Y
                        dst_Y = []
                        while (node.dst != '-1'):
                            node = sentence[int(node.dst)]
                            dst_Y.append(int(node.ID))

                        if len(set(dst_X) & set(dst_Y)) != 0:
                            # XとYのパスが最初に交わるところ
                            cross_point = min(set(dst_X) & set(dst_Y))

                            X = '{0}'.format(re.sub(r'X+', 'X', chunk_X.get_surface()))
                            fout.write('{0}({1})'.format(X, chunk.get_surface()))
                            for chunk_id2 in dst_X:
                                if chunk_id2 == cross_point:
                                    break
                                fout.write(' -> {0}'.format(sentence[chunk_id2].get_surface()))
                            fout .write(' | ')

                            Y = '{0}'.format(re.sub(r'Y+', 'Y', chunk_Y.get_surface()))
                            fout.write('{0}({1})'.format(Y, chunk2.get_surface()))
                            for chunk_id2 in dst_Y:
                                if chunk_id2 == cross_point:
                                    break
                                fout.write(' -> {0}'.format(sentence[int(chunk_id2)].get_surface()))
                            fout.write(' | ')

                            fout.write('{0}\n'.format(sentence[cross_point].get_surface()))



    fin.close()
    fout.close()

    # かかった時間の表示
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")