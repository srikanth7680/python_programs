from collections import ChainMap
a = {'name':'Ramu'}
b = {'Age': 13}
c = ChainMap(a,b)
print(c)
for key,value in c.items():
    print(key,value)
