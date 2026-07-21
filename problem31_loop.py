#write a program to print multiplication table of a given  number using for loop
num =int(input("Enter a number to print multiplication table: "))

for i in range(1,11):
    print(num,"X",i,"=",num*i)