##Nested functions
def add():
    a,b = 10,20
    c = a+b
    print(c)
    def mul():
        d = a*b
        print(d)
    mul()
add()
### Closure functions
def add():
    a,b = 10,20
    c = a+b
    print(c)
    def mul():
        d = a* b
        print(d)
    return mul
ref = add()
ref()
### calculator
def add():
    a = int(input("Enter a number 1: "))
    b = int(input("Enter a number 2: "))
    c = a + b
    print(c)
    def sub():
        d = a-b
        print(d)
    sub()
    def mul():
        e = a * b
        print(e)
    mul()
    def div():
        f = a / b
        print(f)
    div()
add()