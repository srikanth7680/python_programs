from collections import namedtuple
point  = namedtuple('point',['x','y'])
pt1 = point(1,2)
pt2 = point(3,4)
dot_product = (pt1.x*pt2.x+pt1.y*pt2.y)
print(dot_product)
cross_product = (pt1.x*pt2.y+pt1.y*pt2.x)
print(cross_product)
slope=((pt2.y-pt1.y)/(pt2.x-pt1.x))
print(slope)
###
details = namedtuple('employee',('name','age'))
d1 = details("rama",13)
print(d1)
###
employee = namedtuple('employee',('name','Age'))
d2 = employee("Rama",13)
print(d2)