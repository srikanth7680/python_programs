##write a python program that takes a number n as input and generates the first n prime numbers using a for loop
##palindrome check
x = "madam"
if x == (x[::-1]):
    print("palindrome")
else:
    print("not a palindrome")
##Multiplication table
n = int(input("Enter a number: "))
for i in range(1,11):
    print(n ,"*", i, "=", n*i)
