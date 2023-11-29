##1.Write a for loop that prints out the first 10 odd numbers.
'''for x in range(1,21):
    if x%2 != 0:
        print(x)
##2.Write a while loop that counts up from 1 to 20 and prints each number.
i = 1
while i <=20:
    print(i)
    i+=1
##3.Write a for loop that prints out the squares of the numbers from 1 to 10
for i in range(1,11):
    print(i*i)
##4.Write a while loop that asks the user for a number and continues asking until the user enters a positive number.
n = int(input("Enter a number: "))
while n>0:
    print("correct number")
    break
if n<=0:
    print("Enter positive number")
else:
    pass
##5.Write a for loop that iterates over a list of strings and prints each string in uppercase.
a = ["rama","sri","raju"]
for x in a:
    print(x.upper(),end=' ')
##6.Write a while loop that asks the user for a password and continues asking until the correct password is entered.
ans = "Srikanth@123"
while True:
    n = input("enter a password: ")
    if n == ans:
       print("correct password")
       break
    else:
        print("wrong password")
##7.Write a for loop that prints out the first 10 Fibonacci numbers (starting with 0 and 1).
n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
##8.Write a while loop that counts down from 100 to 0 in increments of 10.
count = 100
while count >=0:
    print(count)
    count-=10
##9.Write a for loop that iterates over a list of numbers and prints out the sum of all the numbers.
num = [1,2,3,4,5,6]
sum = 0
for x in num:
    sum+=x
print(sum)
##10.Write a while loop that generates random numbers between 1 and 10 until a number greater than 8 is generated.
import random as rp
i = 0
while i<=8:
    i = rp.randint(1,10)
    print(i)
##11.Write a for loop that prints out the first 20 numbers in the Fibonacci sequence (starting with 0 and 1).
n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(21):
    print(a, end=" ")
    a, b = b, a + b
##12.Write a while loop that asks the user to guess a number between 1 and 10 and continues asking until the correct number is guessed.
import random
correct_number = random.randint(1,10)
guessed_correctly = False
while not guessed_correctly:
    user_guess = int(input("guess a number between 1 to 10"))
    if user_guess == correct_number:
        print("Right guess")
    else:
        print("try again")
##13.Write a for loop that iterates over a list of numbers and prints out the product of all the numbers.
list1 = [1,2,3,4,5]
product = 1
for x in list1:
    product*=x
print(product)
##14.Write a while loop that counts up from 1 to 100, but only prints out the numbers that are divisible by 3.
i = 1
while i<=100:
    i+=1
    if i%3==0:
        print(i)
    else:
        pass
##15.Write a for loop that iterates over a string and counts the number of vowels (a, e, i, o, u) in the string.
n = str(input("Enter a string: "))
vowels = "aeiouAEIOU"
vowel_count = 0
for x in n:
    if x in vowels:
        vowel_count+=1
print(vowel_count)
##16.Write a while loop that asks the user to enter a number and continues asking until the number is between 1 and 100.
x = int(input("Enter a number between 1 and 100: "))
if x > 100:
    x = int(input("Enter a number between 1 and 100: "))
    if x<=100:
        print("correct answer")
    else:
        print("wrong number")
else:
    print("correct answer")
##17.Write a for loop that iterates over a list of strings and prints out only the strings that are longer than 5 characters.
n = ["apple","orange","pineapple"]
for x in n:
    if len(x) > 5:
        print(x)
##1
age = 21
is_student = True
print("age",age)
print("is_student",is_student)
##2
x = int(input("Enter a integer: "))
if x%2 == 0:
    print("Even")
elif x == 0:
    print("zero")
else:
    print("odd")
##3
import math
r = int(input("enter radious: "))
area_of_circle = 3.14*r*r
print(area_of_circle)'''
##
def area_of_circle(r):
    area_of_circle = 3.14(r*r)
    return r
area_of_circle(r)















