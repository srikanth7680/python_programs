a =  int(input("1.Have an issue with transaction"))
if a == 1:
    print("1.Issues with failed payments\n 2.Issues with pending payments\n 3.Issues with succesful payments\n 4.Issues with payments made to merchants\n 5.Issues with friends\n")
    a = int(input("Enter your Option: "))
    if a == 1:
        print("1.Why did my UPI payment fail\n 2.Why is my money deducted for my failed payment\n 3.Why is my money not refunded yet?\n 4.Where can I find the UTR number for this payment?\n")
    a = int(input("Enter the choice: "))
elif a == 2:
    print("1.Why is my UPI payment pending?\n 2.What do I do my UPI payment is pending?\n 3.How do I cancel my pending payment?\n")
    a = int(input("Enter the option: "))
    if a ==1:
        print("Error in your bank")
    else:
        print("Correct")
    if a == 1:
        print("UPI network isssues: ")
    else:
        print("NO issues")
else:
    print("go")


