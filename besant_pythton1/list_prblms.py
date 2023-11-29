##Python program to interchange first and last elements in a list
a = [1,2,3,4,5]
a[0],a[-1] = a[-1],a[0]
print(a)
##Python program to swap two elements in a list
b = [23,65,19,90]
b[0],b[2] = b[2],b[0]
print(b)
##Python – Swap elements in String list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
print("The original list is: " + str(test_list))
res = [sub.replace('G','-').replace('e','G').replace('-','e')for sub in test_list]
print(str(res))
##Python | Ways to find length of list
list = [1,3,4,5,6]
print(len(list))
##Maximum of two numbers in Python
a = 10
b = 3
print(max(a,b))
##Minimum of two numbers in Python
l = [1,2,3,4,5]
print(min(l))
##Python | Ways to check if element exists in list
l1 = [10,20,30,40,50]
i = 0
if i in l1:
    print("it exists")
else:
    print("No it doesn't exists")
##Different ways to clear a list in Python
list1 = [1,2,3,4,5,6]
list1.clear()
print(list1)
##Python | Reversing a List
a = [1,2,3,4,5,6,7]
a.reverse()
print(a)
##Python | Cloning or Copying a list
b = [1,2,3,4,5,6,7,8]
c = b.copy()
print(c)
##Python | Count occurrences of an element in a list
b = [1,2,3,4,1,2,2]
d = b.count(2)
print(d)
##Python Program to find sum and average of List in Python
a = [10,20,30,40,50]
b = sum(a)
print("sum is", b)
avg = b/len(a)
print("Average is ", avg)
##Python | Sum of number digits in List
# Example list of numbers
number_list = [123, 45, 6789, 12]

total_digit_sum = 0

# Iterate through each number in the list
for number in number_list:
    # Convert the number to a string and iterate through each digit
    for digit in str(number):
        # Convert the digit back to an integer and add it to the total
        total_digit_sum += int(digit)

print("Total sum of digit sums:", total_digit_sum)
##Python | Multiply all numbers in the list
l = [1,2,3,4,5]
mul = 1
for i in l:
    mul*=i
print(mul)
##Python program to find smallest number in a list
l = [23,45,67,23,12,2]
m = min(l)
print(m)
##Python Program to Find Largest Number in a List
l = [1,2,3,4,5,6,65]
print(max(l))
##Python program to find second largest number in a list
l = [43,23,56,76,89,90]
l.sort()
print(l[-2])
##Python program to print even numbers in a list
z = [1,2,3,4,5,6,7,8]
for i in z:
    if i%2 == 0:
        print(i,end=',')
    else:
        pass
##Python program to print odd numbers in a List
k = [1,2,3,4,5,6]
for i in k:
    if i%2 != 0:
        print(i,end=',')
##Python program to print all even numbers in a range
n = 10                   #int(input("Enter a number: "))
for n in range(2,n+1,2):
    print(n)
##Python program to print all odd numbers in a range
n = 10                   ##int(input("Enter the number: "))
for n in range(1,n+1,2):
    print(n)
##Python program to count Even and Odd numbers in a List
l = [1,2,3,4,5,6]
m = []
n = []
for i in l:
    if i%2 == 0:
        m.append(i)
    else:
        n.append(i)
print(m,len(m))
print(n,len(n))
##Python program to print positive numbers in a list
l = [2,3,4,-7,-4,-7]
for i in l:
    if i>0:
        print(i,end='')
    else:
        pass
##Python program to print negative numbers in a list
l = [2,3,4,-7,-4,-7]
for i in l:
    if i<0:
        print(i,end=' ')
    else:
        pass
##Python program to print all positive numbers in a range
n = 10
for n in range(1,n+1):
    print(n)
##Python program to print all negative numbers in a range
for i in range(-4,5):
    if i<0:
        print(i)
##Python program to count positive and negative numbers in a list
l = [1,2,3,4,5,6,7,8,9]
m=[]
j = []
for i in l:
    if i%2 == 0:
        m.append(i)
    else:
        j.append(i)
print(m,len(m))
print(j,len(j))
##Remove multiple elements from a list in Python
l = [11, 5, 17, 18, 50,23]
for i in l:
    if i%2 ==0:
        l.remove(i)
    else:
        print(i)
##Python | Remove empty tuples from a list
my_list = [(1, 2), (), (3, 4), (), (), (5, 6)]
f_list=[]
for tup in my_list:
    if tup:
        f_list.append(tup)
print(f_list)
##Remove empty List from List
list2 = [[1, 2], [], [3, 4], [], [], [5, 6]]
empty_list = []
for sublist in list2:
    if sublist:
        empty_list.append(sublist)
print(empty_list)
##
my_list = [[1, 2], [], [3, 4], [], [], [5, 6]]
filtered_list = []
for sublist in my_list:
    if sublist:  # Check if the sublist is not empty
        filtered_list.append(sublist)
print(filtered_list)
###



