class Number:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"value is {self.value} "

    def __add__(self, other):       #dunder method :jab do object k value ko jodna ho tb use krte hai  and print(n1+n2) se call hota hai

        return f"addition ={self.value + other.value}"


n1 = Number(10)
n2 = Number(20)
print(n1)
print(n1 + n2)