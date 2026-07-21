lettet = '''Dear <|NAME|>,
You are selected!
<|DATE|>
'''
name = input("Enter your name:")
date = input("Enter date:")
letter = lettet.replace("<|NAME|>",name).replace("<|DATE|>",date)
print(letter)