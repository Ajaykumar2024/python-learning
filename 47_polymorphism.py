# polymorphism can be achieved by
# -methodoverriding

# here method of child class  overrides the methods of parent class 
# and method of child class executed this is called method overriding
class Animal:
    def show(self):
        print("this is horse")

class Human(Animal):
    def show(self):
        print("this is ajay")

obj=Human()

obj.show()

# Note: in python method overloading does not  exists.