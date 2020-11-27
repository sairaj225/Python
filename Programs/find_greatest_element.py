file_name = input("Enter file name: ")
infile = open(file_name, 'r')
table2 = []

for line in infile:
    row = line.split()
    print(row)
    intRow = []
    for element in row:
        intRow.append(int(element))
    table2.append(intRow)
print(table2)