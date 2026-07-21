# A spam comment is   defined as a text container following keywords "make a lot of money",
#"buy now ","subscribe now", "click this". Write a program to detect this spam

p1="make a lot of money"
p2="buy now"
p3="subscribe now"
p4= "click this"

message= input("Enter you comment :")

if(p1 in message or p2 in message or  p3 in message or p4 in message):
    print("comment is a spam!")
else:
    print("comment is not a spam")