#Create a class
class User: #creates a class named user
    #initialize attributes.
    def __init__(self, user_id, user_name): #In order to be able to add the same attributes to different objects like user_1, user+2 etc we used this
        print("new user being created...") #everytime that we create a new user, this print statement will be triggered
        self.id = user_id #here name of parameter is NOT equal to the attribute
        self.username = username #here name of parameter is equal to the attribute




user_1 = User("001")

print(user_1.username) #prints: Kotha

user_2 = User() #creates object named user_1 using class named User
user_2.id = "002" #adding an attribute for the class named User
user_2.username = "Cutu" #adding another attribute for the class named User

print(user_2.username)