#write a program to print multiplication table of a given number in reverse order
n=int(input("Enter a number:"))
for  i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")

#or
for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")