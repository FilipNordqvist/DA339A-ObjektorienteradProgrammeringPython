class Login():
    def __init__(self,id,password):
        self.id = id
        self.password = password

    def __str__(self):
        return f"ID: {self.id}, Password: {self.password}"