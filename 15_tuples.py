t=(1,2,3,4,5)
print(t)
print(type(t))

t1=()
print(t1)
print(type(t1))

t2=(1,) #for single element tuple we need to add comma
print(type(t2)  )

t3=(12,34,55.5,True,"hello")
print(t3[0]) #accessing first element
print(type(t3)) 
#
# t3[0]=100 #tuples are immutable, we cannot change the value of tuple
