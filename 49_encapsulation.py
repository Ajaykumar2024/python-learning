class Factory:
    a="this is public attribute." #public
    _b="this is protected attribute"    #protected
    __c="this is private attribute"     #private
    def _s(self): #protected
        print(self.__c)

class Human(Factory):
    d="this is child class attribute"
    def show(self):
        print(f"a={self.a}, b={self._b}")

obj=Human()
obj._s()
obj.show()