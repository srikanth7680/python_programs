'''import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Srikanth@123")
print(mydb)'''
##

## using math
import math
print(math.factorial(5))
## without using math
# Python program to find the factorial of a number provided by the user.
num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
##prime numbers
'''n = int(input("Enter a number: "))
if n<=1:
    print("not a prime")
elif n>1:
    for i in range(2,n/):
        if n % i==0:
            print("not a prime number")
            break
        else:
            print("prime number")
else:
    print(n)
## swapping numbers
a = 10
b = 20
a,b = b,a
print(a)
print(b)
##
def swapping(a,b):
    a,b = b,a
    print(a)
    print(b)
n = swapping(2,3)
print(n,end="")
##  string palindrome
a = str(input("Enter a string: "))
if a == a[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")
## maximum numbers
a = [10,20,45,43,56,76,78,9,10]
print(max(a))
##add of two numbers using def
def add(a,b):
    a = 10
    b = 10
    c = a+b
    print(c)
add(2,3)'''
## lamda functions
k = lambda a,b:a+b
print(k(10,20))
##
import math
a = 16
print(int(math.sqrt(a)))
## using function
def sqr(n):
    return n**2
n = sqr(4)
print(n)
## using square
k = lambda a:a**2
print(k(4))
##


