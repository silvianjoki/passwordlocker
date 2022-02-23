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
        
    def delete_user(self):
        '''
        deletes user details from the user list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_username (cls, user_name):
        '''
        Will authenticate the username 
        
        Args:
        returns: user
        '''
        for user in User.user_list:
            if user.user_name == user_name:
                return user
    
    @classmethod
    def user_exists (cls, user_name, password):
        '''
        This will show whether the user exists in the user list information
        
        Returns type boolean for whether user exists 
        Authenticates by using username and password
        
        '''
        for user in cls.user_list:
            if user.user_name == user_name and user.password == password:
                return True
        return False