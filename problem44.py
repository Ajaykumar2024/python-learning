'''
***
**
*
n=3
'''

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print("*" * (n - i + 1))

# #or 
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*",end="") 
#     print() 


#using recursion
def pattern(n):
    if n==0:
        return
    print("*" * n)
    pattern(n-1)

pattern(3)