## alpa(),numeric(),allnum()
'''a = "Ramu"
print(a.isalpha())
b = "123"
print(b.isnumeric())
c = "429abc"
print(c.isalnum())
## password Generator
alpha = ""
digits = ""
spcl = ""
password = input("Enter a password: ")
if len(password)>=8 and len(password)<=15:
    for x in password:
        if x.isalpha():
            alpha+=x
        elif x.isnumeric():
            digits+=x
        else:
            spcl+=x
else:
    print("The password is not in the range 8 to 15")
if len(alpha)>=4 and len(digits)>=1 and len(spcl)>=1:
    print("Password Succesfully completed")
else:
    print("Password is not satisfied")


str = "Rohan"
str2 = "hello"
str2 = str.join(str2)
print(str2)'''

### factorial
n = int(input("Enter a number: "))
i = 1
fac = 1
while i<=n:
    fac= fac * i
    i=i+1
print(fac)
### type casting
a = "Rama12345"
b = ""
for x in a:
    if x.isnumeric():
        b=b+x
    else:
        pass
for y in b:
    k = int(y)
    if k % 2 == 0:
        print(k)
    else:
        pass
##


