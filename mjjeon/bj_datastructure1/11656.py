word = input()
words = []
for i in range(len(word)):
    words.append(word[i:])

print('\n'.join(sorted(words))) 