class User: 
    '''
    this class generates new instances of users
    '''
    
    user_list = []
    
    def __init__(self, user_name, password):
        
        '''
        ags:
        username= user's name
        password = account password
        '''
        self.user_name = user_name
        self.password = password
        
    def save_user(self) : 
        # this is to save the user's information 
        
        User.user_list.append(self)
