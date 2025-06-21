text = input("Text: ")
words = text.split()
words_to_count = {}
for word in words:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1

