#write a program to find whether a given user name contains less than 10 characters or not

user_name= input("Enter username:")
if(len(user_name)<10):
    print("Your username contains less than 10 characters")
else:
    print("Your username contain greater than or equal to 10 characters")