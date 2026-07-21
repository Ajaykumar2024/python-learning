# Write a program to input eight number from the user and display all the unique numbers(once)

number=set()
for i in range(8):
    num=int(input("enter the number:"))
    number.add(num)

print(number)