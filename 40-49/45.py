# -*- coding: utf-8 -*-

import morph

if __name__ == '__main__':
    fin = open("neko.txt.cabocha", "r")

    texts = morph.file2texts(fin)
    sentences = []
    [sentences.append(morph.text2chunks(text)) for text in texts]

    predicate = ''
    head = morph.Chunk([], '', '')

    fout = open('45result.txt', 'w')
    write_flg1 = False
    write_flg2 = False


#    for sentence in sentences:
        for chunk in sentence[7]:
            if '動詞' in [morph.pos for morph in chunk.morphs]:
                for morph in chunk.morphs:
                    if morph.pos == '動詞':
                        predicate = morph.base
                        head = chunk
                        write_flg1 = True
        cases = []
        for chunk in sentence[7]:
            if chunk.dst == head.dst:
                for morph in chunk.morphs:
                    if morph.pos == '助詞':
                        cases.append(morph.surface)
                        write_flg2 = True

        if write_flg2 and write_flg1:
            fout.write(predicate + '\t')
            [fout.write(case + ' ') for case in cases]
            fout.write('\n')
            write_flg1 = False
            write_flg2 = False

