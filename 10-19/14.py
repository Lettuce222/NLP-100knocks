import sys

argvs = sys.argv
N = int(argvs[1])
fr = open('hightemp.txt', 'r')

for low in fr:
    print low,
    N -= 1
    if N == 0 :
        break