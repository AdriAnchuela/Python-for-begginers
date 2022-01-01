# Fibonacci 1 1 2 3 5 8 13

x = int(input('How many fibonacci numbers do u want to print out: '))

fib = []

e=1
r=1
if x==0:
    print(fib)
elif x==1:
    fib.append(1)
    print(fib)
else:
    for i in range(2):
        
        fib.append(e)
    for i in range(x-2):
        e=e+r
        fib.append(e)
        r=e-r
    print(fib)
    
# Other solution
#def gen_fib():
#   count = int(input("How many fibonacci numbers would you like to generate? "))
#   i = 1
#   if count == 0:
#       fib = []
#  elif count == 1:
#        fib = [1]
#  elif count == 2:
#        fib = [1,1]
#    elif count > 2:
#        fib = [1,1]
#       while i < (count - 1):
#           fib.append(fib[i] + fib[i-1])
#           i += 1
#
#   return fib