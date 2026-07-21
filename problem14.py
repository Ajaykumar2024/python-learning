# write a program to store five fruits in a list entered by the user
fruits=[]
# f1=input("enter  fruit name")
# fruits.append(f1)
# f2=input("enter  fruit name")
# fruits.append(f2)
# f3=input("enter  fruit name")
# fruits.append(f3)
# f4=input("enter  fruit name")
# fruits.append(f4)
# f5=input("enter  fruit name")
# fruits.append(f5)
# print(fruits)

#another trika 

for i in range(5):
    fruit=input(f"enter fruit name {i+1} :")
    fruits.append(fruit)

print("list of fruits :",fruits)
