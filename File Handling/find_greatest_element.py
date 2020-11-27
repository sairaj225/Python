# Reading file name
file_name = input("Enter file name: ")
# Opening file with read mode
infile = open(file_name, 'r')
table2 = []

# Reading table content into 2D list
for line in infile:
    row = line.split()
    intRow = []
    for element in row:
        intRow.append(int(element))
    table2.append(intRow)

print(f"File {file_name} converted to 2D list...")
[print(list) for list in table2]

# Reading N value for comparison
N = int(input("Enter an integer or 0 to quit: "))

# While loop is executs untile user enters 0
while(N!=0):
    count = 0
    for list in table2:
        for element in list:
            if element>N:
                count = count + 1
    print(f"There are {count} elements greater than {N}.", end="\n\n")
    N = int(input("Enter an integer or 0 to quit: "))


    