# -*- coding: utf-8 -*-

import morph

if __name__ == '__main__':
    fin = open("neko.txt.cabocha", "r")

    texts = morph.file2texts(fin)
    sentences = []
    [sentences.append(morph.text2chunks(text)) for text in texts]

    predicate = ''
    head = morph.Chunk([], '', '')

    fout = open('48result.txt', 'w')
    write_flg1 = False
    write_flg2 = False

    for i, sentence in enumerate(sentences):
        fout.write('{0}\n'.format(i+1))

        for chunk_id, chunk in enumerate(sentence):
            if '名詞' in [morph.pos for morph in chunk.morphs]:
                chunk_X = chunk
                changed_flg = False
                for j, morph in enumerate(chunk_X.morphs):
                    if morph.pos != '助詞':
                        morph.surface = 'X' if changed_flg else ''
                        changed_flg = True

                for chunk2 in sentence[chunk_id+1:]:
                    if '名詞' in [morph.pos for morph in chunk.morphs]:
                        chunk_Y = chunk
                        changed_flg = False
                        for j, morph in enumerate(chunk_X.morphs):
                            if morph.pos != '助詞':
                                morph.surface = 'Y' if changed_flg else ''
                                changed_flg = True

                fout.write('{0}'.format(chunk.get_surface()))
                node = chunk

                # 根へのパスの出力
                while( True ):
                    if node.dst == '-1':
                        break
                    node = sentence[int(node.dst)]
                    fout.write(' -> {0}'.format(node.get_surface()))

                fout.write('\n')


    fin.close()
    fout.close()

