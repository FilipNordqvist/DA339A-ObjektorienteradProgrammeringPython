class Person():
    def __init__(self, name, age):
        self._name = name
        self.age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        self._name = new_name
    
    
 