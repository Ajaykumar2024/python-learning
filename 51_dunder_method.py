'''
The word dunder means Double UNDERscore.
A dunder method is a special method in Python whose name starts and ends with double underscores (__).
These methods are also called magic methods or special methods because Python calls them automatically when certain operations are performed.
__init__
__str__
__len__
__add__
__repr__
'''

class Student:
    def __init__(self,name):        #dunder method :called when object is created
        self.name=name
    def __str__(self):              #dunder method : called when object is printed
        return f"hello student name is {self.name}"
    def __add__(self,others):
        return self.name+others.name


s=Student("ajay")
s2=Student("vijay")
print(s)
print(s+s2)
# print(s.name)