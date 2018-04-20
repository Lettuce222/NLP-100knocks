import re
import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = re.split('[ ]', str)
result = []

for word in words:
    if len(word) > 4:
        word = word[0] + ''.join(random.sample(word[1:len(word)-1], len(word)-2)) + word[len(word)-1]
    result.append(word)
    
result_str = ' '.join(result)

print(result_str)