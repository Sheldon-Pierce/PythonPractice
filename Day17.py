class User:
    """Models the user"""
    def __init__(self, username):
        self.name = username
        self.id = 0
        self.followers = 0
        self.following = 0

    def change_username(self, new_username):
        self.name = new_username

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('Sheldon')
user_2 = User('Silver')
print(user_1.name)
user_1.change_username('Shelly P')
print(user_1.name)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)