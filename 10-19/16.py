import sys

argvs = sys.argv
N = int(argvs[1])
fr = open('hightemp.txt', 'r')

lines = fr.readlines()

fr.close()

fws = []
for i in range(N):
    fw = open('16result-' + str(i+1), 'w')
    fws.append(fw)

num_lines = sum(1 for line in open('hightemp.txt'))

for i in range(N):
    for j in range(num_lines/N):
        fws[i].write(lines[i*num_lines/N + j])