def char_ngram(str,n):
    result = []
    
    for i in range(len(str)-(n-1)):
        gram = ()
        for j in range(n):
            gram += tuple(str[i+j])
        result.append(gram)
    
    return result
    
str1 = "paraparaparadise"
str2 = "paragraph"

X = set(char_ngram(str1,2))
Y = set(char_ngram(str2,2))

print(X|Y)
print(X&Y)
print(X-Y)

print("se in X?",('s','e') in X)
print("se in Y?",('s','e') in Y)