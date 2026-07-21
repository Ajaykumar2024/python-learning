marks={
"name":"ajay",
"rohan":45,
"shayam":99
}

print(marks.get("name"))
# print(marks["vijay"])

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"rohan":99 , "age":25} )
print(marks)

# marks.clear() #clear all items
# print(marks) 

b=marks.copy()
print(b)

b.pop("name")
print(b)
a=b.popitem()
print(b)
print(a)