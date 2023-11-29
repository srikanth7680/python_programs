amount = int(input("Enter the Amount"))
years = int(input("How many years"))
print("Available loans \n 1.farmer_loans\n 2.car_loan\n 3.home_loan")
loan = int(input("Which loan do you want"))
if loan == 1:
    interest = (amount * years *.1)
elif loan == 2:
    interest = (amount * years *.18)
elif loan == 3:
    interest = (amount * years *.85)
print ("Simple Interest",interest)