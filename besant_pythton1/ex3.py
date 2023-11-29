sal = int(input("Enter the range of TV manufacture: "))
if sal >=0 and sal<=10:
    amount = 1
    total_amount = (amount * 82)
elif sal >=10 and sal<=20:
    amount = 1.5
    total_amount = (amount * 82)
elif sal > 20:
    amount = 2
    total_amount = (amount * 82)
print("The Indian salary is", total_amount)

