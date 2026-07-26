class Animal:
    name="lion"     #class attributes
    def __init__(self,age):
        self.age=age        #instance attributes
    def show(self):         #instance methods: it(self) targets object location 
        print(f"how are you! you age is {self.age}")

    @classmethod        #this(@) is a decorator
    def hello(cls):     #class method :it(cls) target class location
        print("how are you brother")
        print(cls.name)


    @staticmethod
    def static_method(): #it cannot access or modify the class attribute and intance attribute
        print("This is static method")
Animal.hello()
obj=Animal(23)
obj.show()
# obj.hello()
Animal.static_method()