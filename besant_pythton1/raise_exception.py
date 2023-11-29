##
try:
    percentage = int(input())
    if percentage< 0 or percentage> 100:
        raise Exception
    else:
        print(percentage)
except Exception:
    print("Percentage is Invalid")
##Username
user_name=[]
try:
    user_id = int(input())
    if user_id not in user_name:
        user_name.append(user_id)
    else:
        raise Exception  ("input no spl character spl character")
    password = input()

    if len(password)>=4 and len(password)<=8:
        raise Exception  ("no spl character spcl character")
    for x in password:
        if x.isalnum():
            pass
        else:
            raise Exception  ("no spl character spcl character")
except Exception as E1:
    print("E1")
###
try:
    age = int(input())
    gender= input()
    if age<=18 or gender != "Male" and gender != "Female" and gender != "Transgender":
        raise Exception ("Invalid")
    else:
        print("correct details")
except Exception as E2:
    print(E2)
##Attribute Error
try:
    x = input("Enter a number: ")
    if x == int(x):
        print("correct")
except ValueError as e:
    print("ValueError",e)


