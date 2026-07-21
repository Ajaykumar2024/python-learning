#write a function to to print multiplication table of a given number n
def table(n):
     for i in range (1,11):
         print(f"{n} X {i} = {n*i}")
table(5)