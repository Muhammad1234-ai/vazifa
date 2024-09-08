file = open("salom.txt", "r")

malumot = file.readlines()

if malumot:
    print(malumot[-1])

file.close()
