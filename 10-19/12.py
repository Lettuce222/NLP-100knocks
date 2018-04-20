fr = open('hightemp.txt', 'r')
fw1 = open('col1.txt', 'w')
fw2 = open('col2.txt', 'w')

for low in fr:
    words = low.split('\t')
    fw1.write(words[0] + '\n')
    fw2.write(words[1] + '\n')
    
fr.close()
fw1.close()
fw2.close()