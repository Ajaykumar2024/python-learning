class Factorymumbai:
    a='I am a attribute mentioned inside factory'
    def hello(self):
        print("I am a method mentioned inside Factory ")

class FactoryPune(Factorymumbai):
    pass

obj=Factorymumbai()

# print(obj.a)
# obj.hello()
obj2=FactoryPune()
obj2.hello()