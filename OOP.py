# Object oriented programming

# Knowing the type of the object

def hello():
    print('hello')

x = 1
print(type('hello'))
print(type(x))
print(type(hello))

#The program will print the type 
# of the object we are reffering to

#Functions might not work if the objets are
# of different types

y = 'hello'
# print (x+y) /// This will give us an error

print(y.upper()) # That is called method and 
                # u can use them 
                # next to different objects


class Dog:
    def add_one(self,x):
        return x + 1
    def bark(self):
        print('bark')

d = Dog()
d.bark()
print(type(d))
print(d.add_one(5))

