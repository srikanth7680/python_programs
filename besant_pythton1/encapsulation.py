##
class emp:
    def __init__(self,salary):
        self._salary=salary
        print("inside the class",salary)
    def getter(self):
        return self._salary
    def setter(self,salary):
        self._salary=salary
        print(self._salary)
sri=emp(1000)
print("outside the class",sri.salary)