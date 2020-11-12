line = input()
words = line.split()
for i, word in enumerate(words):
    print(i, word[:10])