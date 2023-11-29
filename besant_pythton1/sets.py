##
a = [10,1,3,6,1,11]
b = set(a)
c = list(b)
print(c)
print(set(list(a)))
##
f = "rama is going to school"
for x in f:
    if x in 'aeiou':
        print(x,end='')
    else:
        pass
##add()
b = {10,20,30}
b.add(100)
print(b)
##update()
b = {10,20,30}
c={11,21,30}
b.update(c)
print(b)
##remove and delete
b = {10,20,30}
b.remove(10)
print(b)
##delete
b={10,20,30}
del b
print(b)
##intersection
b = {10,11,10}
c={11,30}
e = b.intersection(c)
print(e)
