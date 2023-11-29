## Removing duplicates without using set
b = []
a = [10,1,1,3,2,1]
for x in a:
    if x in b:
        pass
    else:
        b.append(x)
print(b)
### or using set removing duplicate
print(list(set(a)))
##
courseA = { 10,1,3,6,2}
courseB = {10,1,300,400}
print(courseA.intersection(courseB))
####union
print(courseA.union(courseB))
print(courseA|courseB)
##difference
print(courseA.difference(courseB))
###symmetric difference
print(courseA.symmetric_difference(courseB))
###
a = {10,1,3,6,2}
b = {10,1,300,400}
c = {1,3,6,7,9}
##1from 3 tables how many are common taken admission
print(a.intersection(b,c))
##4.extract how many people are present in all courses
print(a.union(b,c))
###3.How many persons take only one course
print(a.difference(b,c))
##2

