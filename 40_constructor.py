class Factory:
    def __init__(self,material, zip,pocket):        #Initialization (constructor)
        self.material=material
        self.zip=zip
        self.pocket=pocket
    def show(self):
        print(f"your object details are : {self.material},{self.zip},{self.pocket}")

reboke=Factory("lather",2,3)        #object 1
campus=Factory("nylon",3,3)         #object 2
 
reboke.show()