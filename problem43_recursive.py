#Write a recursive function to calculate the sum of first  n natural numbers.
def sum_natural_numbers(n):
    if n==1:
        return 1
    else:
        return n + sum_natural_numbers(n-1)
    
n = int(input("Enter a number: "))
print(f"sum of first {n} natural number is :{sum_natural_numbers(n)}")