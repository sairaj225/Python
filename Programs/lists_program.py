
list_a=[]
list_b=[]
print("List a Elements:")
data = input("Enter an element or press enter to finish: ")
while(data!=""): 
    list_a.append(data)
    data=input("Enter an element or press enter to finish: ")
print("List b Elements:")
data = input("Enter an element or press enter to finish: ")
while(data!=""): 
    list_b.append(data)
    data=input("Enter an element or press enter to finish: ")
listb=list_b.copy()
list_b.reverse()
length_a =len(list_a)
length_b = len(list_b)
result_list = []
i=length_a
j=length_b
m=0
n=0
for k in range(length_a+length_b):
    if i>0 and j>0:
        if k%2==0:
            result_list.append(list_a[m])
            i = i-1
            m=m+1
        else:
            result_list.append(list_b[n])
            j=j-1
            n=n+1
    elif j>0 and i==0:
        result_list.append(list_b[n])
        j=j-1
        n=n+1
    elif i>0 and j==0:
        result_list.append(list_a[m])
        i=i-1
        m=m+1
print(list_a)
print(listb)
print(result_list)