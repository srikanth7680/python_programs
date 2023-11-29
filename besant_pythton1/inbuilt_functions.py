##math module
import math
a = 16
print(math.sqrt(a))
### Random modules
import random
print(random.randint(1,10))
# choice is a package
import random
a = ["a","b","c","d"]
print(random.choice(a))
## datetime module
import datetime
print(datetime.datetime.now())
## eulers number
import math
print(math.e)
## pi
print(math.pi)
## "Tau" is defined as the ratio of the circumference to the radius of a circle.
print(math.tau)
## area of circle
import  math
r = 4
pie = math.pi
area = pie * r * r
print(area)
## square root of any number
s = 16
print(math.sqrt(s))
### infinity
print(math.inf)
## ceil and floor functions
a = 2.3
print("The ceil of a is ",math.ceil(a))
print("The floor of a is ",math.floor(a))
##factorial of any number
a = 4
print(math.factorial(a))
## GCD of any number
print(math.gcd(15,5))
## fabs() function returns the absolute value of the number.
a = -10
print((math.fabs(a)))
##pow() function computes x**y. This function first converts its arguments into float and then computes the power.
print(pow(2,3))
'''## math module performs
1.sqrt
2.pie
3.ceil and floor
4.pow()
5.GCD
6.factorial
7.fabs
8.infinity'''
### Random modules
import random
print(random.randint(10,15))
## It generates the  random number range between 0 and 1
print(random.random())
## if you set the seed(3) it results always same number without generating random values
random.seed(0)
print(random.randint(1,1000))
'''##Random module performs
1. It generates the  random number range between 0 and 1
2. if you set the seed(3) it results always same number without generating random values'''

## datetime modules
import datetime
print(datetime.datetime.now())
## find the today date
print(datetime.date.today())
## timestamp
print(datetime.datetime.timestamp(1887639468))
##
print(datetime.date.fromisoformat(2023 - 36 - 0o2))
'''## datetime modules performs
1.datetime
2.today date and today time 
3.timestamp
4.convert date to string'''