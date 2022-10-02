#Create a class
class User: #creates a class named user
    #initialize attributes.
    def __init__(self, user_id, username): #In order to be able to add the same attributes to different objects like user_1, user+2 etc we use this
        print("new user being created...") #everytime that we create a new user, this print statement will be triggered
        self.id = user_id #here name of parameter is NOT equal to the attribute
        self.username = username #here name of parameter is equal to the attribute
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1 #when followed, user_2's followers increase
        self.following += 1 #when followed, user_1's following increase


user_1 = User("001", "Kotha",)
print(user_1.id) #prints "001"
user_2 = User("002", "Cutu")
print(user_2.username) #prints: "Cutu

user_1.follow(user_2)
print(user_1.followers) #prints: 0
print(user_1.following) #prints: 1
print(user_2.followers) #prints: 1
print(user_2.following) #prints: 0