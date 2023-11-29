##memory space for strings
'''a = "rama"
b = "rama"
print(id(a))
print(id(b))
##slicing
val = "Ramaraj"
print(val[3:5]) ##output- ar
print(val[4:]) ## output- raj
print(val[::1]) ## output-Ramaraj
print(val[::-1]) ## output- jaramaR
val2 = "madam"
if val2[::1] == val2[::-1]:
    print("palindrome")
else:
    print("Not palindrome")
##f-strings
user = input("Enter the name: ")
age = int(input(f"{user} enter the age"))
print(a,b)
         ##or
b = int(input("{} enter your age".format(user)))
print(a,b)'''
##ex1
lst = [40,50,20,30,90]
a = lst[1:3]
print(a)
##ex2
lst = list(range(30,100,10))
print(lst)
print(lst[2:6])
##ex3
lst = list(range(10))
print(lst)
print(lst[2:6:2])
##ex4
a = list(range(10))
print(a[:-2])
##ex5
a = list(range(10))
print(a[:-2:2])
##
import math
def area(radious):
    area_of_circle = math.pi * radious**2
    return area_of_circle
radious = float(input("Enter a radious"))
result = area(radious)
print(result)


