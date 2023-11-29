##Armstrong number
num = 153
sum = 0
temp= num
while temp>0:
    digit = temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print("armstrong")
else:
    print("not Armstrong")
##Fibanacci series  
n = 4
a,b = 0,1
print("Fibanacci series")
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b
print("\n")
## String Reversal in python
string = 'srikanth'
print(string[::-1])
##Reverse of a program
num = 1234
rev_num = 0
while num !=0:
    digit = num%10
    rev_num = rev_num*10 + digit
    num //=10
print(rev_num)
## printing right angled triangle
n = 5
for i in range(1,n+1):
    print("* " * i)
## printing triangle pattern
n = 5
for i in range(1,n+1):
    spaces = " " * (n-i)
    stars = "* " * i                                                
    print(spaces + stars)
##Fibanacci series
n = 11
a,b = 0,1
for i in range(1,n + 1):
    print(a,end=' ')
    a,b = b,b +a
##remove duplicates in the program
l1 = [1,2,2,3,4,4,5,6,6]
print(set(l1))
##convert binary to decimal
a = '1010'   ##Binary value
b = int(a,2) 
print(b)
## convert decimal to binary
a = 10
b = print(bin(a)[2:])
##Reverse a number program
num = '1212'
number = int(num[::-1])
print(number)
### perfect number or not 
num = 28
sum = 0
for i in range(1,num):
    if num%i == 0:
        sum = sum + i
if sum == num:
    print("Perfect")
else:
    print("Not perfect")

##
n = int(input("Enter a number: "))
for i in range(2,n):
    if n%i == 0:
        print("Not prime year")
        break
else:
    print("Prime number")