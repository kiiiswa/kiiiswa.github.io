class User:
    # Define the fields and methods for your object here.
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.users = []
        self.connections = []


    def add_user(self, users):
        user_input2= input("which user would you like to add?")
        self.users.append(user_input2)

    def print_users(self):
        print (self.users)

    def add_connection(self, connections):
        user_input3= input("which user would you like to form a connection?")
        if user_input3 in self.users:
            self.connections.append(user_input3)


class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.posts = []
        self.users = []

    def add_posts(self, post):
        self.post.append(post)

    def show_post(self, post):
        print ()

start = '''
welcome to the social network!
'''


def main():
    # Define the program flow for your user interface here.
    kiswa = User("kiswa", "oct 21")
    internet = Network()
    print (start)
    done = False
    while not done:
        user_input = input("type nu to add a new user, c to make a connection, p to add a post")
        if user_input == "nu":
            kiswa.add_user()
        if user_input == "c"
            kiswa.add_connection()



    print(kiswa.name)

# Runs your program.
#if __name__ == '__main__':
main()
print ("kiswa")
