import morph

if __name__ == '__main__':
    fin = open("neko.txt.cabocha", "r")

    texts = morph.file2texts(fin)
    sentences = []
    [sentences.append(morph.text2chunks(text)) for text in texts]

    for sentence in sentences:
        for chunk in sentence:
            if int(chunk.dst) != -1:
                print(chunk.get_surface().strip('、。') + '\t' + sentence[int(chunk.dst)].get_surface().strip('、。'))