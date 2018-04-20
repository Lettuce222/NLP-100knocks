import re

def word_split(str):
    _words = re.split('[ ]', str)
    words = []

    for word in _words:
        words.append(word.strip(',.'))
    
    return words

def word_ngram(str,n):
    words = word_split(str)
    result = []
    
    for i in range(len(words)-(n-1)):
        gram = []
        for j in range(n):
            gram.append(words[i+j])
        result.append(gram)
    
    return result

def char_ngram(str,n):
    result = []
    
    for i in range(len(str)-(n-1)):
        gram = []
        for j in range(n):
            gram.append(str[i+j])
        result.append(gram)
    
    return result
    
str = "I am an NLPer"

word_bigram = word_ngram(str,2)
char_bigram = char_ngram(str,2)

print(word_bigram)
print(char_bigram)
    