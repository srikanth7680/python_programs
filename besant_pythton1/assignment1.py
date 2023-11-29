##1.print 1 to 10 numbers
i = 1
while i <= 10:
    print(i)
    i = i+1
##2.pattern
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
##3.Calculate the sum of all numbers from 1 to a given number
x = int(input("Enter a number: "))
total = x * (x+1)/2
print(int(total))
##4.Write a Python program to check if a number is positive, negative or zero.
n = int(input("Enter a number: "))
if n > 0:
    print("Positive Number")
elif n < 0:
    print("Negative Number")
else:
    print("Equals to zero")
##5.Write a Python program to check if a number is even or odd.
y = int(input("Enter a number: "))
if y%2 == 0:
    print("Even number")
else:
    print("Odd number")
##6.Write a Python program to find the largest of three numbers.
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))
if n1>=n2 and n1>=n3:
    print("n1 is larger")
elif n2>=n1 and n2>=n3:
    print("n2 is larger")
else:
    print("n3 is larger")
##7.Write a Python program to check if a year is a leap year.
year = int(input("Enter year: "))
if year%400 == 0 and year%100 == 0:
    print("Leap year")
elif year%4 == 0 and year%100 != 0:
    print("Leap year")
else:
    print("Not leap year")
##8.Write a Python program to check if a character is a vowel or consonant.
letter = str(input("Enter a letter: "))
if letter in ('a','i','e','o','u','A','E','I','O','U'):
    print("Vowel")
else:
    print("Consonant")
##1.Write a Python program to calculate the sum of two numbers. If the sum is between 15 and 20, return 20.
n1 = int(input("Enter a number1: "))
n2 = int(input("Enter a number2: "))
sum = n1 + n2
if sum >=15 and sum<=20:
    print("20")
else:
    print(sum)
##2.Write a Python program to check if a given number is a prime number or not.
n = int(input("Enter a number: "))
for i in range(2,n):
    if n%i == 0:
        print("Not prime year")
        break
else:
    print("Prime number")
##3.Write a Python program to print the Fibonacci series up to a given number.
nterms = int(input("Enter upto n terms: "))
n1,n2 = 0,1
count = 0
if nterms <= 0:
    print("Enter positive number")
elif nterms == 1:
    print("Fibanacci upto: ")
    print(n1)
else:
    print("Fibanacci Series")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count+=1
##4.Write a Python program to check if a given string is a palindrome or not.
x = input("Enter a string: ")
if x == x[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
##5.Write a Python program to print the multiplication table of a given number.
z = int(input("Enter a number: "))
for i in range(1,11):
    print(z ,'x', i, '=' ,z*i)

##6.Write a Python program to check if a given number is an Armstrong number.
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
   print(num,"is not an Armstrong number")
##7.Write a Python program to find the sum of all even numbers between 1 to 100.
total_sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        total_sum += num
print("The sum of even numbers between 1 and 100 is:", total_sum)
##8.Write a Python program to find the maximum and minimum values in a given list of numbers.
numbers_list = [34, 12, 45, 78, 23, 56, 9, 101]
max_value = numbers_list[0]
min_value = numbers_list[0]
for num in numbers_list:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("The maximum value is:", max_value)
print("The minimum value is:", min_value)
##9.Write a Python program to check if a given number is a perfect square or not.
number = int(input("Enter a number: "))
square_root = number ** 0.5
if square_root == int(square_root):
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")
##10.Write a Python program to check if a given number is a palindrome or not without using string manipulation.
number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")
##11.Write a Python program to check if a given string is a pangram or not.
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
unique_alphabets = set()
for char in sentence:
    if char.isalpha():
        unique_alphabets.add(char)
if len(unique_alphabets) == 26:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
##12.Write a Python program to check if a given number is a Harshad number or not.
number = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(number))
if number % sum_of_digits == 0:
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
##13.Write a Python program to check if a given number is an abundant number or not.
number = int(input("Enter a number: "))
divisors_sum = 0
for i in range(1, number):
    if number % i == 0:
        divisors_sum += i
if number < divisors_sum:
    print(f"{number} is an abundant number.")
else:
    print(f"{number} is not an abundant number.")
##14.Write a Python program to find the GCD (Greatest Common Divisor) of two numbers using recursion
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
result = gcd(num1, num2)
print(f"The Greatest Common Divisor (GCD) of {num1} and {num2} is:", result)
##15.Write a Python program to check if a given number is a strong number or not.
number = int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
sum_of_factorials = sum(factorial(int(digit)) for digit in str(number))
if number == sum_of_factorials:
    print(f"{number} is a strong number.")
else:
    print(f"{number} is not a strong number.")
##16.Write a Python program to check if a given number is a perfect number or not.
number = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, number // 2 + 1):
    if number % i == 0:
        sum_of_divisors += i
if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
##17.Write a Python program to print the first n terms of the Fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b










