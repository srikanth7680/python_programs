##
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Not possible")
finally:
    print("finally keyword will execute everytime")
except ValueError:
    print("string not possible")
except IndexError:
    print("not defined")
##NameError
try:
    variable_name = 23
    print(varible_name)
except NameError as e:
    print("NameError",e)
##RuntimeError
def infinite_recursion():
    return infinite_recursion()
try:
    infinite_recursion()
except RecursionError as e:
    print("RecursionError:",e)




