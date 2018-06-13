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

        for chunk in sentence:
            if '名詞' in [morph.pos for morph in chunk.morphs]:
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

