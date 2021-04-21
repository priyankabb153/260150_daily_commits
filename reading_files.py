file = open("myfile.txt", "r")
# This determines the number of bytes that should be read.
print(file.read(16))
print(file.read(4))
cont = file.read()
print("re-reading")
print(cont)
print("finished")
file.close()

# to retrive each line
# print(file.readlines())

file = open("myfile.txt", "r")

for line in file:
    print(line)

file.close()