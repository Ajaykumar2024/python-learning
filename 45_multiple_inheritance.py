class Animal:
    def __init__(self,name):
        self.name=name

class Human:
    def  __init__(self,name,age):
        super().__init__(name)
        self.age=age

class Robots(Human,Animal):   #inheritance order imp.:-jis bhi constructor ko target krwana hai us class ko pahle inherit krenge
    def show(self):
        print(f"you name is {self.name},age= {self.age}")

r=Robots("ajay",34)
r.show()