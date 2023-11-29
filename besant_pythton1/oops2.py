class demo:
    def show(self):
        a = 30
        b = 60
        c = a + b
        if c > 30:
            return 0
        else:
            return 1
d1 = demo()
d2 = d1.show()
print(d2)
## method accepting parameters and no return values
class Atm:
    def check_balance(self,pin):
        balance = 3000
        if pin == "123":
            q = int(input("1.check balance\n2.withdraw\n"))
            if q == 1:
                print("bal",balance)
            else:
                print("Enter correct pin")
sbi = Atm()
sbi.check_balance("123")
## static variable
class Farmer:
    r = 10
    def loan(self):
        p = int(input("Enter principle amount: "))
        t = int(input("Enter period of time: "))
        simple_interest = p*t*Farmer.r/100
        print(simple_interest)
f1 = Farmer()
f1.loan()
###
class library:
    def lending_books(self):
        global books
        books=["the mind"]
        print(books)
    def accepting(self):
        print(books)
a = library()
a.lending_books()
a.accepting()
###


