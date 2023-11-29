##functions
def add():
    a = 10
    b = 20
    c = a+b
    print(c)
add()
##
def mul(x,y):
    c = x*y
    print(c)
x = int(input("Enter 1 number:"))
y = int(input("Enter 2 number:"))
mul(x,y)
##keywords and arguments
def sum(name,sal):
    print("sal",sal)
    print("name",name)
sum(name="rama",sal=1000)
## It accept so many parameters
def demo(*a):
    print(a)
demo(10,20,30)
##
def sum(x,y):
    c=y-x
    print(c)
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
sum(y,x)
