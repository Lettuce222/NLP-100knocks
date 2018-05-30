import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
        self.all = [self.surface, self.base, self.pos, self.pos1]
    def print_all(self):
        print(','.join(self.all))

class Chunk:
    def __init__(self, morphs, dst, ID):
        self.morphs = morphs
        self.dst = dst.strip('D')
        self.ID = ID
        self.srcs = []
        self.all = [self.morphs, self.dst, self.ID, self.srcs]
    def print_all(self):
        [print(morph.surface, end='') for morph in self.morphs]
        print(' ' + self.ID + ',' + self.dst + ',' + '*'.join(self.srcs))
    def get_srcs(self, chunks):
        srcs = []
        for chunk in chunks:
            if chunk.dst == self.ID:
                srcs.append(chunk.ID)

        return srcs
    def get_surface(self):
        result = ""
        for morph in self.morphs:
            result = result + morph.surface
        return result

def file2texts(file):
    texts= []
    text = []
    for (i, line) in enumerate(file):
        text.append(line)
        if line == 'EOS\n':
            texts.append(text)
            text = []
    return texts

# 解析情報を分節ごとに分ける
def devide_text(text):
    result = []
    chunk = []

    for (i, line) in enumerate(text):
        if line[0] == '*' and i != 0:
            result.append(chunk)
            chunk = []
        if line != 'EOS\n':
            chunk.append(line)

    if len(chunk) != 0:
        result.append(chunk)

    return result

def text2morphs(text):
    morphs = []

    for (i, line) in enumerate(text):

        m = re.search(r"(.*)\t(.*)", line)

        if m:
            surface = m.group(1)
            other = m.group(2)

            if surface != "EOS":
                morphs.append(Morph(surface, other.split(',')[6], other.split(',')[0], other.split(',')[1]))

    return morphs

def text2chunks(text):
    chstrs = devide_text(text)
    chunks = []

    for chstr in chstrs:
        chunks.append(Chunk(text2morphs(chstr), chstr[0].split(' ')[2], chstr[0].split(' ')[1]))

    for chunk in chunks:
        chunk.srcs = chunk.get_srcs(chunks)

    return chunks



