#Ask the user for a string and print out whether this string is a palindrome or not.

x = str(input('Write a word or a phrase: '))

list1 = []
list2 = []
for c in x:
    list1.append(c)
    list2.append(c)

list2.reverse()

print(list1)
print(list2)
if list1 == list2:
    print('It is a palindrome')

else:
    print('It is NOT a palindrome')