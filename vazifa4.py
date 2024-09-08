file1 = open("me.txt", "r")
data = file1.read()

file1.close()

file2 = open("mee.txt", "w")
file2.write(data)

file2.close()
