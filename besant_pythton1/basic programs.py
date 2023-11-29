##Python program to add two numbers
num1 = 10
num2 = 20
sum = num1 + num2
print(sum)
##Maximum of two numbers in Python
num1 = 30
num2 = 1
if num1 > num2:
    print("num1 is max")
else:
    print("num2 is great")
##Python Program for factorial of a number
n = 6
fact = 1
for i in range(1,n + 1):
    fact*=i
print(fact)
##Python Program for simple interest
p = int(input("Enter the princple amount: "))
t = int(input("Enter the time: "))
r = int(input("Enter the rate of interest: "))
simple_interest = (p*t*r)/100
print(simple_interest)
##Python Program for compound interest
p = int(input("Enter the princple amount: "))
R = float(input("Enter the rate of interest: "))
t = int(input("Enter the time: "))
a = p*(1+(R/100))**t
ci = a - p
print(ci)
##Python Program to check Armstrong Number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
    print(num,"not a palindrome")
##Python Program for Program to find area of a circle
x = float(input("Enter a number: "))
pi = 3.14
area = pi * (x ** 2)
print(area)
##Python program to print all Prime numbers in an Interval








