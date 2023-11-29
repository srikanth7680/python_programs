### for loop in range
'''x = int(input("enter a number: "))
y = int(input("Enter a number: "))
for i in range(x,y):
    sum = 0
    for j in range(i):
        sum = sum + j
        print(i,'total sum',sum)'''
## for loop
'''sum = 0
for i in range(1,200,2):
    sum = sum + i
    print(sum,'sum of odd numbers')'''

### while loop
i = 0
while i < 200:
    print(i**3)
    i = i+1