#Write a program using function to convert celsius to fahrenheit.

def celsius_to_fahrenheit(celsius):
   return (celsius * 9/5) + 32
     

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius) #function call

print(f"{celsius}°C is equal to {round(fahrenheit, 2)}°F") 