#file handling 
# p=open(r'C:\Users\askaj\OneDrive\Documents\!-- rating --.txt')
# p=open('41_file_handling.py')
# print(p.read())


# i want to create a file: using ''w'

r=open('superman.txt','a')
# r.write('hello this is Ajay and I am learnig python') #file me write krta hai or ager baad me kuckk add krege to override kr dega
r.write('and Now I am appending some content on file !') #append krne k liye file ko 'a' mode me open krna hoga

r.close()
