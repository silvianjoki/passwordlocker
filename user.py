class User: 
    
    # this class generates a new user instance
    
    user_list = []
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    def save_user(self) : 
        # this is to save the user's information 
        
        User.user_list.append(self)
