#write a program to detect double spaces in a string 
a="This is a string  with double  spaces."
if "  " in a:
    print("Double spaces detected.")        



    # ya
    print(a.find("  ")) # it will give the index of first 
                             #occurrence of double space

    print(a.replace("  "," "))
     
   
