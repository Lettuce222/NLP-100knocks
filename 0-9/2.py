# -*- coding: utf-8 -*-

str1 = "パトカー"
str2 = "タクシー"

list = []

for i in range(len(str1)):
    list.append(str1[i])
    list.append(str2[i])

print("".join(list))