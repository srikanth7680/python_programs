## pandas functions
'''import pandas as pd
l1 = pd.Series([10,20,30,40,50])
print(l1)
## changing indexes
l1 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(l1)
## series object from dictionaries
l2 = pd.Series({'a':100,'b':200,'c':300,'d':400})
print(l2)
##changing index for dictionaries
l2 = pd.Series({'a':100,'b':200,'c':300,'d':400},index=['d','c','a','e'])
print(l2)
## Extracting individual elements
a = l1[3]
print(a)
## extracting a sequence elements
b = l1[:4]
print(b)
## Extracting elements from back
c = l1[-3:]
print(c)
## basic math operations
m = l1 +1
print(m)
m = l1 - 1
print(m)
m = l1 * 2
print(m)
## adding 2 series
l1 = pd.Series([10,20,30,40,50])
l2 = pd.Series([1,2,3,4,5])
l3 = l1 + l2
print(l3)
l3 = l1 - l2
print(l3)
l3 = l1 * l2
print(l3)'''

##
import pandas as pd
df1 = pd.DataFrame({'Name':['srikanth','manoj','ramu','raju'],'marks':[90,80,70,75]})
print(df1)
l1 = df1.head()
print(l1)
l1 = df1.tail()
print(l1)
l1 = df1.shape
print(l1)
l1 = df1.describe()
print(l1)
l1 = df1.iloc[0:3,0:2]
print(l1)
l1 = df1.loc[1:3,('marks')]
print(l1)
l1 = df1.drop('marks',axis=1)
print(l1)
l1 = df1.drop([1,2],axis=0)
print(l1)