#program to accet marks of six student  and display them into a sorted manner

marks=[]
f1=int(input("enter  mark here"))
marks.append(f1)
f2=int(input("enter  mark here"))
marks.append(f2)
f3=int(input("enter  mark here"))
marks.append(f3)
f4=int(input("enter  mark here"))
marks.append(f4)
f5=int(input("enter  mark here"))
marks.append(f5)
f6=int(input("enter  mark here"))
marks.append(f6)
print(marks)

marks.sort()
print("marks in sorted order:",marks)

#another trika 

# for i in range(6):
#     mark=int(input(f"enter marks here {i+1} :"))
#     marks.append(mark)

# marks.sort()
# print("list of marks :",marks)
