# -*- coding: utf-8 -*-

import morph

if __name__ == '__main__':
    fin = open("neko.txt.cabocha", "r")

    texts = morph.file2texts(fin)
    sentences = []
    [sentences.append(morph.text2chunks(text)) for text in texts]

    predicate = ''
    head = morph.Chunk([], '', '')

    fout = open('47result.txt', 'w')
    write_flg1 = False
    write_flg2 = False

    for i, sentence in enumerate(sentences):
        # fout.write('{0}\n'.format(i+1))

        for chunk in sentence:
            for morph in chunk.morphs:
                if morph.pos == '動詞':
                    predicate = morph

                    # 述語に係る助詞を集める
                    items = {}
                    continue_flg = True
                    for chunk2 in sentence:
                        if chunk2.ID in chunk.srcs:
                            for j, morph2 in enumerate(chunk2.morphs):
                                if morph2.pos == '助詞':
                                    if morph2.surface == 'を'\
                                    and chunk2.morphs[j-1].pos == '名詞'\
                                    and chunk2.morphs[j-1].pos1 == 'サ変接続':

                                        continue_flg = False
                                        sahen_surface = chunk2.morphs[j-1].surface + morph2.surface + predicate.base
                                        continue

                                    items[morph2.surface] = chunk2.get_surface()

                    if continue_flg:
                        continue

                    # 結果を出力
                    if not len(items) == 0:
                        fout.write('{0}\t'.format(sahen_surface))
                        [fout.write('{0} '.format(case)) for case in sorted(items.keys())]
                        fout.write('\t')
                        [fout.write('{0} '.format(items[case])) for case in sorted(items.keys())]
                        fout.write('\n')

    fin.close()
    fout.close()

