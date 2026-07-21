#Write a program to find a factorial of a number using for loop

num=int(input("intera a number:"))
fact=1

for i in range(1,num+1):
    fact=fact*i
print("Factorial of ",num,"is:", fact)
    