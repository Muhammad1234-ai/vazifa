file = open("salom.txt", "r")

malumot = file.read()

words = malumot.split()
longest_word = max(words, key=len)
print(longest_word)

file.close()
