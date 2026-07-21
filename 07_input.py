a = input("Enter a number: ")   # This will take the input as a string
b = input("Enter another number: ") # This will also take the input as a string

print("Number a=",a)
print("Number b=",b)
print("The sum=", a+b)          # This will now add the two numbers as strings
# To fix this, we need to convert the input to integers
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("sum=", a+b)               # This will now add the two numbers as integers