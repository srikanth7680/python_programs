##
user = input("Enter 'yes' if you want pizza: ")
pizzas=[]
prices=[]
if user.lower() == "yes":
    print("1.corn pizza\n2.cheese pizza\n3.veg pizza\n")
    while True:
        ordered_pizzas = input("Enter which pizza you want or cancel the pizza: ")
        if ordered_pizzas.lower() == "cancel":
            break
        pizzas.append(ordered_pizzas)
        if ordered_pizzas.lower() == 'corn pizza':
            prices.append(120)
        elif ordered_pizzas.lower() == 'cheese pizza':
            prices.append(150)
        elif ordered_pizzas.lower() == 'veg pizza':
            prices.append(200)
    total_amount = sum(prices)
    print("ordered_pizzas",pizzas)
    print("pizza prices",prices)
    print("total_amount",total_amount)
    print("thank you for visiting")
else:
    print("Thank you")



