myfile = open("myfile.txt")
#  If the file is in the current working directory of the program,
#  you can specify only its name.


"""
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.
"""
# write mode
open("write.txt", "w")
# write mode creates a file is not present

# read mode
open("myfile.txt", "r")
# open("read.txt")

# binary write mode
open("filename.txt", "wb")
# wb mode also creates files when not present

# rb is binary read mode

"""
You can use the + sign with each of the modes above to give them 
extra access to files.
For example, r+ opens the file for both reading and writing.
"""

file = open("write.txt", "w")
# do stuff
file.close()
