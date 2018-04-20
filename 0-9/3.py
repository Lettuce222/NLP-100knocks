str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = str.split()
word_nums = []

for word in words:
    word = word.strip(',.')
    word_nums.append(len(word))

print(words)
print(word_nums)