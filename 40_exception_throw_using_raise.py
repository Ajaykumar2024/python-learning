age = int(input("Enter your age: "))
try:
    if age<10 or age>18:
        raise ValueError("Age should be between 10 and 18") # raise keyword is used to throw an exception
    else:
        print("welcome to club")   
except Exception as err:           
    print(f"error occur : {err}") 


print("the club will start soom! ")