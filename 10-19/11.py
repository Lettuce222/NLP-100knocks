fr = open('hightemp.txt', 'r')
fw = open('11result.txt', 'w')

for low in fr:
    for c in low:
        if c =='\t' :
            c = ' '
        fw.write(c)
        
fr.close()
fw.close()