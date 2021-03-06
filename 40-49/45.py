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

    for i, sentence in enumerate(sentences):
        fout.write('{0}\n'.format(i+1))

        for chunk in sentence:
            for morph in chunk.morphs:
                if morph.pos == '動詞':
                    predicate = morph

                    # 述語に係る助詞を集める
                    cases = []
                    for chunk2 in sentence:
                        if chunk2.ID in chunk.srcs:
                            [cases.append(morph2.surface) for morph2 in chunk2.morphs if morph2.pos == '助詞']

                    # 結果を出力
                    if not len(cases) == 0:
                        fout.write('{0}\t'.format(predicate.base))
                        [fout.write('{0} '.format(case)) for case in cases]
                        fout.write('\n')

    fin.close()
    fout.close()

