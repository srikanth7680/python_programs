a =10
b=10
if a<b:
    print("a is greater")
elif b<a:
    print("b is greater")
else:
    print("Both are great")

## new code
sub1 = int(input("Enter the social marks"))
sub2 = int(input("enter the maths marks"))
sub3 = int(input("Enter the CS marks"))
sub4 = int(input("enter the science marks"))
sub5 = int(input("Enter the English marks"))
sub6 = int(input("Enter the Kannada marks"))
all_subject_marks = (sub1+sub2+sub3+sub4+sub5+sub6)/6
if all_subject_marks < 35:
    print("Fail")
elif all_subject_marks in range(35,51):
    print("C grade")
elif all_subject_marks in range(51,81):
    print("B grade")
elif all_subject_marks in range(81,91):
    print("A grade")
elif all_subject_marks in range(91,101):
    print("A+ grade")
else:
    print("Enter correct marks")
