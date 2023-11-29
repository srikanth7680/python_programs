a =  int(input("1.Have an issue with transaction"))
if a == 1:
    print("1.Issues with failed payments\n 2.Issues with pending payments\n 3.Issues with succesful payments\n 4.Issues with payments made to merchants\n 5.Issues with friends\n")
    a = int(input("Enter your Option: "))
    if a == 1:
        print("1.Why did my UPI payment fail\n 2.Why is my money deducted for my failed payment\n 3.Why is my money not refunded yet?\n 4.Where can I find the UTR number for this payment?\n")
    a = int(input("Enter the choice: "))
    if a == 1:
        print("UPI incorrect")
        if a == 2:
            print("It will be refunded in 2 days")
            if a == 3:
                print("UTR transaction send")
                if a == 4:
                    print("In the HIstory")
    elif a == 2:
            print("1.Why is my UPI payment pending?\n 2.what do I do my UPI payment is pending?\n 3.How do I cancel my pending request?\n")
            a = int(input("Enter your option: "))
            if a == 1:
                print("We recommended that you wait for 48hrs from the time of payment")
                if a == 2:
                    print("After 48hrs bank may update the the status of your pending payment")
                    if a == 3:
                         print("You can't cancel UPI payments once intiated")
    elif a == 3:
            print("1.Payments made to a phone number or UPI ID\n 2.Payments made to a bank account\n")
            a = int(input("Enter your option: "))
            if a == 1:
                print("It succesfully debited")
                if a == 2:
                     print("amount credited to the bank account")
    elif a == 4:
            print("1.What if the merchant denies having recieved the amount for a succesful payment?\n 2.What if I have paid a twice for an order or booking?\n 3.What if the order or booking is not confirmed for a successful payment?\n")
            a = int(input("Enter the option: "))
            if a == 1:
                print("please tap the button below and create a ticket for relevant payment")
                if a == 2:
                    print("Raise a complaint with a UTR number for the relevant payment")
                if a == 3:
                    print("we request you to contact directly  for an update")
    elif a == 5:
            print("1.Refund for UPI payments\n 2.Refunds for card payments\n3.Refunds for payments made to a merchant\n")
            a = int(input("Enter your option: "))
            if a == 1:
                print("Within the 3 to 5 days from the date you made the payment")
                if a == 2:
                    print("Within the 7 to 9 days from the date you made the payment")
                    if a == 3:
                        print("We request that you contact the merchant directly")
    else:
        print("Enter correct option")


