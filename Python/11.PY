
x = 25 #global scope variable

def my_func():
    x = 50 
    return x

print(x)
print(my_func())


name = 'This is a global name!'

def greet():
    name = 'Aman' #enclosing function locals used only in this function

    def hello():
        print("hello "+name)
    hello()

greet()
print(name)

def func():
    global x
    x = 1000

print("before func call x is ",x)
func()
print("After func call x is ",x)