import sys

argvs = sys.argv
N = int(argvs[1])
fr = open('hightemp.txt', 'r')

lines = fr.readlines()

fr.close()

for i in range(N):
    print lines[len(lines) - N + i],