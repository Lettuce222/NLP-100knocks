import re

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
_words = re.split('[ ]', str)
words = []

for word in _words:
    words.append(word.strip(',.'))

initial_nums = [1,5,6,7,8,9,15,16,19]
dict_result = {}

print(words)

for i in range(len(words)):
    word = words[i]
    if i in initial_nums:
        dict_result[word[0]] = i
    else:
        dict_result[word[0:2]] = i

print(dict_result)
    
