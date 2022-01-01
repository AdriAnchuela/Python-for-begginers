# Write a program (function!) that takes a list and returns a 
# new list that contains all the elements of the first list minus 
# all the duplicates.

lista = [1,2,2,2,3,4,7,5,6,6,6,7,9,0,1,3,2,4,5,6,4,4,3,8]

def nodup (list):
    newlist = []
    for i in list:
        if i in newlist:
            newlist.remove(i)
        newlist.append(i)
    newlist.sort()
    print (newlist)

nodup(lista)