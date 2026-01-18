class LoginHandler:
    def __init__(self, max_elements):
        self.login_list = []  # Skapar en tom lista
        self.num_of_elements = 0  # Startar utan några element
        self.max_elements = max_elements


    #Lägger till login i listan om det finns plats.
    def add_new(self, login):
        success = True

        # Om login inte är None och antalet element är mindre än max → då går det att lägga till.
        if login is not None and self.num_of_elements < self.max_elements:
            self.login_list.append(login)
            self.num_of_elements += 1
        else:
            print("List is full")
            success == False

        return success

    #Tar bort element med hjälp av index
    def remove_elements_at(self,index):
        success = True
        
        if index < 0 or index >= self.num_of_elements:
            success = False
            
        else:
            self.login_list.pop(index)
            self.max_elements -= 1

        
        return success

    #Returnerar längden på listan
    def get_numers_of_elements(self):
        return len(self.login_list)
