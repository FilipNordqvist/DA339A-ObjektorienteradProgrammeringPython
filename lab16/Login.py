class Login():
    def __init__(self,id,password):
        self.id = id
        self.password = password

    def to_string(self):
        print(f"ID: {self.id}, Password: {self.password}")