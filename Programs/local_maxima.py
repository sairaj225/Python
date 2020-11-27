data = [3, 6, 1, 2, 5, 4, 9, 5, 7, 2, 4]

print('List of found local maxima: ')
for i in range(1, len(data)-1):
    if data[i-1]<data[i]>data[i+1]:
        print(f'{data[i]} at position {i}')