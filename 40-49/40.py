import morph

if __name__ == '__main__':
    fin = open("neko.txt.cabocha", "r")

    texts = morph.file2texts(fin)
    sentences = []
    [sentences.append(morph.text2morphs(text)) for text in texts]

    [morph.print_all() for morph in sentences[2]]
