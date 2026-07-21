#Create an empty dictionary .Allow 4 friends to enter their favorite language
#as value and use key as their name .
d ={}

for i in range(4):
    friend=input("Enter the friend name :")
    lang=input("Enter faviorate language:")
    d.update({friend:lang})

print(d)