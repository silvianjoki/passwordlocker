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
    
    def save_credentials (self):
        
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
        '''
        return Credentials.credentials_list
    
    @classmethod
    def find_by_app_name( cls, app_name):
        '''
        Method that takes in the app_name and returns the credentials that matches the app
        Args:
        app_name- name of application 
        
        returns:
        Credentials matching the application
        '''
        for credential in Credentials.credentials_list:
            if credential.app_name == app_name:
                return credential
            

    @classmethod
    def display_credential(cls,password):
        '''
        Method that returns the credential list
        Args:
        acccount_password : password
        '''
        user_credential_list = []
        
        for credential in cls.credentials_list:
            if credential.account_password == password:
                user_credential_list.append(credential)
            
            return user_credential_list

    @classmethod
    def credentials_exist(cls, app_name):
        '''
        Method resolves the presence of credentials in the credentials list
        
        Args:
        app_name - name to display if the account is in existence
        
        Returns:
        Type boolean
        '''
        for credential in Credentials.credentials_list:
            if credential.app_name == app_name:
                return True
        return False