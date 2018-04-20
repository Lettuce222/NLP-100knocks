def cipher(str):
    return ''.join(map(_cipher, str))

def _cipher(char):
    if 'a' <= char and char <= 'z' :
        return chr(219 - ord(char))
    else:
        return char

str = u"hello,World222"

print cipher(cipher(str))


        