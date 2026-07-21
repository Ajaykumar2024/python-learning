#write a program to find whether a given name is present in list or not
name_list=["ajay","vikram","akif","subodh"]

name=input("enter name:")

if(name in name_list):
    print("name is present in list ")
else:
    print("name is not present in list")