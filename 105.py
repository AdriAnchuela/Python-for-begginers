#Divisors

x = int(input('Get divisors of number...'))

for i in range(1,x):
    if x%i==0:
        print(i)

