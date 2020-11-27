#TODO: Demonstrate mergin of two files

dataOne = dataTwo = ""

# Reading data from file1
with open( "file1.txt" ) as fp:
    fileOneData = fp.read()

# Reading data from file2
with open( "file2.txt" ) as fp:
    fileTwoData = fp.read()

# Mergin two files
fileOneData += '\n'
fileOneData += fileTwoData

with open( "file3.txt", 'w' ) as fp:
    fp.write( fileOneData )
