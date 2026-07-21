m1=int(input("enter mark of subject 1:"))
m2=int(input("enter mark of subject 2:"))
m3=int(input("enter mark of subject 3:"))

total_percentage=((m1+m2+m3)/300)*100

if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are passed by",total_percentage ,"%")
else:
    print("you failed!, try next time:",total_percentage ,"%")
