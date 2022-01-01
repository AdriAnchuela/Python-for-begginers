#List overlap, return a list that includes the numbers that are in common between both lists without dupicates

list1 = [1,1,2,3,5,8,13,21,34,55,89]

list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

newlist = []

for i in list1:
    if i in list2 and i not in newlist:
        newlist.append(i)

print(newlist)