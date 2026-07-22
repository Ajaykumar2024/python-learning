# polymorphism using duck typing
# in the talk() ,we don't care it is a Duck or Human .we only care that both object has talk()method


class Duck:
    def talk(self):
        print("Quack")

class Human:
    def talk(self):
        print("hello")

obj1=Duck()
obj2=Human()

obj1.talk()
obj2.talk()