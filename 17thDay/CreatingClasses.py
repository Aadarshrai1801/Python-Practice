# Creating Classes

class User :
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user) :
        user.follower += 1
        self.following += 1   


# Creating object 'user1'

user1 = User(2331178, 'Aadarsh')

# Creating attributes 'id' & 'username' 

# user1.id = "2331178"
# user1.username = "Aadarsh"

print(user1.id, user1.username, user1.follower)

# Creating object 'user2'

user2 = User(233181, 'Adarsh')

# Creating attributes 'id' & 'username'

# user2.id = "233179"
# user2.username = "Ayush"

print(user2.id, user2.username, user2.follower)

# Adding Methods to class

user1.follow(user2)
print(user1.follower)
print(user1.following)

print(user2.follower)
print(user2.following)