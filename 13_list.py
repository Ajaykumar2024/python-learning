#list are mutable,means we can change the value of the list after it is created
friend=["Alice", "Bob", "Charlie", 7, False, 42, None]

print(friend)

friend[2]="ajay"
print(friend)

friend.append("David") #append() method is used to add an element at the end of the list
print(friend)