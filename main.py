#Create a class
class User: #creates a class named user
    #initialize attributes.
    def __int__(self): #In order to be able to add the same attributes to different objects like user_1, user+2 etc we used this
        print(f"new user being created")




user_1 = User() #creates object named user_1 using class named User
user_1.id = "001" #adding an attribute for the class named User
user_1.username = "Kotha" #adding another attribute for the class named User

print(user_1.username) #prints: Kotha

user_2 = User() #creates object named user_1 using class named User
user_2.id = "002" #adding an attribute for the class named User
user_2.username = "Cutu" #adding another attribute for the class named User