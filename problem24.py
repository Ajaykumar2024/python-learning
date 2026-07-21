#write a program to find greatest among 4 number entered by user

a1=int(input("enter number 1:"))
a2=int(input("enter number 2:"))
a3=int(input("enter number 3:"))
a4=int(input("enter number 4:"))

if(a1>a2 and a1>a3 and a1>a4):
 print("a1 greatest number:",a1)

elif(a2>a1 and a2>a3 and a2>a4):
 print("a2 greatest number:",a2)

elif(a3>a2 and a3>a1 and a3>a4):
 print("a3 greatest number:",a3)

elif(a4>a2 and a4>a3 and a4>a1):
 print("a4 greatest number:",a4)