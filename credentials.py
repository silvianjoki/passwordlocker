import random
from signal import default_int_handler
# import choice
import string

class Credentials: 
    '''
    this class generates a new instance of credentials
    '''
    
    credentials_list = []
    
    def __init__(self, app_name, account_username, account_password) -> None:
        
        self.app_name = app_name
        self.account_username = account_username
        self.account_password = account_password
    
    def add_credentials (self):
        
        '''
        this will add new credentials to the credentials list
        '''
        Credentials.credentials_list.append(self)
        
    def delete_credentials (self):
        '''
        this will delete credentials from the credential list
        '''
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def display_credentials(cls, username):
        '''
        this method displays the credential list
        
        returns the user
        '''
        user_user_list = []
        for user in user.user_list:
            if user.username == username:
                return user
        