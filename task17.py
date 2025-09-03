class Session:
    def __init__(self):
        self.username = None
    
    def login(self, username):
        self.username = username
        print(f"{self.username} logged in")
    
    def logout(self):
        if self.username:
            print(f"{self.username} logged out")
            self.username = None
        else:
            print("No user logged in")



s = Session()
s.login("Ali")
s.logout()
