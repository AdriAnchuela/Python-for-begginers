#List less than 10
#List less than 10 creating another list

list = [1,1,2,3,5,8,13,21,34,55,89]

list2 = []

for x in list:
    if x<10:
        list2.append(x)
        print(x)

print(list2)