class Animal:
    name="lion"     #class attributes
    def __init__(self,age):
        self.age=age        #instance attributes
    def show(self):         #instance methods: it(self) targets object location 
        print(f"how are you! you age is {self.age}")

    @classmethod        #this(@) is a decorator
    def hello(cls):     #class method :it(cls) target class location
        print("how are you brother")

    @staticmethod
    def static_method():
        print("This is static method")

obj=Animal(23)
# obj.show()
# obj.hello()
obj.static_method()