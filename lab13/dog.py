class Dog():
    
    def __init__(self,age,gender,name):
        self.age = age
        self.gender = gender
        self.name = name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        try:
            self.age = int(age)
        except ValueError:
            print("Ålder måste vara en siffra")
                
        
    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender
        
    def get_name(self):
        return self.name

    def set_name(self, name):
        if not name.strip():
            raise ValueError("Vänligen ange ett namn")
        self.name = name
        
    
    
    