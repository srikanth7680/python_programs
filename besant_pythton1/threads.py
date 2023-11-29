##
import time
class task1:
    def show(self):
        x = ["rama","raja","ravi"]
        for i in x:
            print(i)
            time.sleep(1)
class task2:
    def numbers(self):
        for i in range(5):
            print(i)
class task3:
    def maths(self):
        x = 10
        y = 12
        print("addition",x+y)
        print("sub",x-y)
        print("mul",x*y)
        print("div",x%y)
a = task1()
a.show()
b = task2()
b.numbers()
c = task3()
c.maths()
##
import time
from threading import *
class task1(Thread):
    def run(self):
        x = ["rama","raja","ravi"]
        for i in x:
            print(i)
            time.sleep(3)
class task2(Thread):
    def run(self):
        for i in range(5):
            print(i)
            time.sleep(3)
class task3(Thread):
    def run(self):
        x = 10
        y = 12
        print("addition",x+y)
        time.sleep(3)
        print("sub",x-y)
        time.sleep(3)
        print("mul",x*y)
        time.sleep(3)
        print("div",x%y)
        time.sleep(3)
a = task1()
a.start()
b = task2()
b.start()
c = task3()
c.start()
## Multi threading
'''import time
from threading import *
class meta(Thread):
    def run(self):
        print("receiving")
        time.sleep(3)
class whats_app(Thread):
    def run(self):
        print("send the messages in whats app!")
        time.sleep(3)
class insta(Thread):
    def run(self):
        print("send the messages in insta!")
        time.sleep(3)
class facebook(Thread):
    def run(self):
        print("send a messages in fb")
        time.sleep(3)
a = meta()
a.start()
time.sleep(3)
b = whats_app()
b.start()
time.sleep(3)
c = insta()
c.start()
time.sleep(3)
d = facebook()
d.start()
time.sleep(3)'''
