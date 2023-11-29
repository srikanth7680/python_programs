'''b = (10,20,30)
print(type(b))
b[0] = 100
print(b)
##
b = (10,[20],30,[100,200])
print(type(b))
##
d=[]
c=[]
b= (10,[20],30,[100,200])
for x in b:
    if type(x) == list:
        c.append(x)
    else:
        d.append(x)
print(c)
print(d)
##1
a = ["rama",10,20,100,30]
b = []
for x in a:
    if type(x) == str:
        b.append(x)
    else:
        b.append(x)'''
##1
a = ["rama",10,20,100,30]
b =[]
for x in a:
    if type(x) == str:
        b.append(x)
    else:
        b.append(x)
print(b)
##2
b = [10,20,100,31]
c = []
for x in b:
    if x%2==0:
        c.append(x)
    else:
        pass
d = sum(c)
print(d)
##3
b = [10,20,100,200]
c = [30,60,70,100]
d = max(b)
e = max(c)
f = max(b) + max(c)
print(f'{d} + {e} = {f}')
##4
b = [10,20,100,200]
c =[]
c.append(max(b))
c.append(min(b))
total = sum(c)
print(total)
##5
b = ["rama","ra","ra"]
for x in b:
    print(len(x))
##6
c = ["Rama is going","worked on book"]
result = []
for x in c:
    words = x.split()
    length = [len(word) for word in words]
    result.append(length)
print(result)
##7
f = [23,65,75]
results = [sum(int(digit) for digit in str(num)) for num in f]
print(results)
##7
'''g = str(f)
for x in g:
    x+=x
    print(x,end='')'''
##8
f = [111,101,105,117]
m = []
f = str(f)
y = f.split()
print(y)
##9
f = [10,20,60,70,30]
f.sort()
print(f[1])
print(f[-2])
##10
f = ["rama",10,20,3,2]
for x in f:
    print(len(str(x)),end=" ")
