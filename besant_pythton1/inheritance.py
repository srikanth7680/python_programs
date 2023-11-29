##
class cargo_plane():
    def carry_goods(self):
        print("Carry goods")
    def fly(self):
        print("flying")
    def take_off(self):
        print("take_off")
    def landing(self):
        print("landing")
class passenger(cargo_plane):
    def carry_passenger(self):
        print("Carry passenger")
class fighter_jet(cargo_plane):
    def carry_weapon(self):
        print("Carry weapon")
c1 = cargo_plane()
c1.carry_goods()
c1.fly()
c1.take_off()
c1.landing()
c2 = passenger()
c2.carry_passenger()
c2.fly()
c2.take_off()
c2.landing()
c3 = fighter_jet()
c3.carry_weapon()
c3.fly()
c3.take_off()
c3.landing()
##Method Overriding-same method names but different parameters is called as method overriding.
class weeklyplan_hotel:
    def show(self):
        print("12 members")
    def show1(self):
        print("13 members")
    def show2(self):
        print("15 members")
class day1(weeklyplan_hotel):
    def show(self):
        print("16 members")
class day2(weeklyplan_hotel):
    def show1(self):
        print("17 members")
class day3(weeklyplan_hotel):
    def show2(self):
        print("18 members")
a = weeklyplan_hotel()
a.show()
a.show1()
a.show2()
b = day1()
b.show()
c = day2()
c.show1()
d = day3()
d.show2()
##Method Overloading-Different methods but same parameters is called as method overloading
# Python program to demonstrate
# multiple inheritanc3
# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)
# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)
# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()





