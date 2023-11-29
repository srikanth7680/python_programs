## dominos
'''total_pizzas = ["corn pizza","cheese pizza","chicken pizza","panner pizza","mushroom pizza","millmaker pizza"]
amount = [100,120,130,140,99,160]
user_input = input("which pizza do you want? ")
order_pizza = []
order_pizza.append(user_input)
print(order_pizza, amount[0], "rupees")
for user_input in total_pizzas:
    if user_input == [0]:
        print(amount[0])
        order_pizza+=order_pizza
order_pizza.append(user_input)
print(order_pizza, amount[0], "rupees")
pizza = ["corn pizza","chicken pizza"]
price = [100,200]
for x in pizza:
    print(x)
##
a = [100,200,30,40,60]
b = max(a)
print(b)
c = min(a)
print(c)
a.sort()
print(a[-1])'''
##
ans = input("Enter 'yes' if you want to order pizzas: ")
if ans.lower() == "yes":
    Dominos_pizzas = []
    Dominos_pizzas_Rate = []
    print("Pizzas available: \n01) corn pizzas - Rs250, \n02) chicken pizzas - Rs350, \n03) capsicum pizzas - Rs500")
    while True:
        ordered_pizzas = input("Enter the pizza you want (or 'done' to finish ordering): ")
        if ordered_pizzas.lower() == "done":
            break
        Dominos_pizzas.append(ordered_pizzas)
        if ordered_pizzas == "corn pizzas":
            Dominos_pizzas_Rate.append(250)
        elif ordered_pizzas == "chicken pizzas":
            Dominos_pizzas_Rate.append(350)
        elif ordered_pizzas == "capsicum pizzas":
            Dominos_pizzas_Rate.append(500)
    total_amount = sum(Dominos_pizzas_Rate)
    print("Ordered pizzas:", Dominos_pizzas)
    print("Pizza prices:", Dominos_pizzas_Rate)
    print("Total amount: ", total_amount)
    print("Thank you for visiting!")
else:
    print("Thank you for visiting!")

