#Write a function to convert inches to cm

def inches_to_cm(inches):
    return inches * 2.54
n = float(input("Enter length in inches: "))
print(f"{n} inches = {inches_to_cm(n)} cm") #function call