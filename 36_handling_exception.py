a=int(input("Enter a number: "))

try:                        # try block will check for the error and if there is an error it will go to except block
    print(10/a) 
except Exception as err:    #or except ZeroDivisionError: (except block will catch the error and store it in variable err
    print(f"there is an error: {err}") # this will excute if error occurs in try block
else:                       # else block will execute if there is no error in try block
    print("there is no exception    ")
finally:                   # finally block will execute no matter what
    print("I will run no matter what")

print("ok, I have done the division ")
 