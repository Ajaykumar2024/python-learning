e=set()  #empty set

print(e,type(e)) 
# e.add(12)
 
number ={1,2,3}
print(number)
number.add(7)
print(number)

number.update([8,9,10,"mango"])
print(number)
number.remove(10)
print(number)
number.discard("mango")
print(number)

item=number.pop()
print(item)
print(number)

number.clear()
print(number)



