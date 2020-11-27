print("List a Elements:")
list_a=[]
list_b=[]
data = input("Enter an element or press enter to finish: ")
while(data!=""): 
    list_a.append(int(data))
    data=input("Enter an element or press enter to finish: ")
print("List b Elements:")
data = input("Enter an element or press enter to finish: ")
length_a = len(list_a)
length_b = len(list_b)
while(data!=""): 
    
    list_b.append(int(data))
    data=input("Enter an element or press enter to finish: ")
list_b.reverse()
if length_a==length_b:
    result_list = [sub[item] for item in range(length_b) 
                      for sub in [list_a, list_b]] 
elif length_a > length_b:
    result_list = [sub[item] for item in range(length_b) 
                      for sub in [list_a, list_b]] 
    remain = length_a-length_b
    remaining_elements = list_a[remain+1:length_a]
    result_list.extend(remaining_elements)

elif length_b > length_a:
    result_list = [sub[item] for item in range(length_b) 
                      for sub in [list_a, list_b]] 
    remain = length_b-length_a
    remaining_elements = list_b[remain+1:length_b]
    result_list.extend(remaining_elements)

print(result_list)