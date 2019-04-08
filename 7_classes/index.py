class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def show_fullname(self):
        print(self.first_name + ' ' + self.last_name)

user1 = User("John", 'Malkovich')
user1.show_fullname()

print(user1.last_name)