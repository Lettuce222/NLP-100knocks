import CaboCha

def write_f1(line, f):
    cp = CaboCha.Parser("")
    tree = cp.parse(line)
    f.write(tree.toString(CaboCha.FORMAT_LATTICE))


if __name__ == '__main__' :
    fin = open("neko.txt", "r")
    fout = open("neko.txt.cabocha", "w")

    for line in fin:
        write_f1(line, fout)