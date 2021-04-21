file = open("write.txt", "w")
file.write("this should be written to file")
file.close()

file = open("write.txt", "r")
cont = file.read()
print(cont)
file.close()

# The "w" mode will create a file, if it does not already exist.

file = open("myfile.txt", "r")
print("reading contents")
print(file.read())
print("finished")
file.close()

file = open("myfile.txt", "w")
file.write("writing new contents to myfile.txt")
print("finished writing")
file.close()

file = open("myfile.txt", "r")
print("reading contents after writing something")
print(file.read())
file.close()

# As you can see, the content of the file has been overwritten.

msg = "hello world!"
print(len(msg))
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
# To write something other than a string, it needs to be converted to a string first.

try:
    f = open("newfile.txt")
    print(f.read())
finally:
    f.close()

# This ensures that the file is always closed, even if an error occurs.
print("new way")
with open("newfile.txt") as f:
    print(f.read())

# The file is automatically closed at the end of the with statement, even if exceptions occur within it.