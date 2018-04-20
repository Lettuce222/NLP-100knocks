fr1 = open('col1.txt', 'r')
fr2 = open('col2.txt', 'r')
fw = open('13result.txt', 'w')

for (low1,low2) in zip(fr1,fr2):
    fw.write(low1[:-1] + '\t' + low2)

fr1.close()
fr2.close()
fw.close()