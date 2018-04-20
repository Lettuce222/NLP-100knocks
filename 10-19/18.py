fr = open('hightemp.txt', 'r')
fw = open('18result.txt', 'w')

lines = fr.readlines()
datas = []

for line in lines:
    datas.append(line.split('\t'))

datas.sort(key = lambda x: x[2], reverse = True)

for data in datas:
    fw.write('\t'.join(data))

fr.close()
fw.close()
    
