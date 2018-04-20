fr1 = open('hightemp.txt', 'r')
fr2 = open('col1.txt', 'r')
fw = open('19result.txt', 'w')

lines1 = fr1.readlines()
lines2 = fr2.readlines()

fr1.close()
fr2.close()

col1_data = [[e, lines2.count(e)] for e in set(lines2)]

col1_data.sort(key = lambda x:x[1], reverse = True)

datas = [line.split('\t') for line in lines1]

for (name, i) in col1_data:
    for data in datas:
        print (name[:-1],data[0])
        if name[:-1] == data[0]:
            fw.write('\t'.join(data))