
import random
import string


class Credentials: 
    '''
    this class generates a new instance of credentials
    '''
    
    credentials_list = []
    
    def __init__(self, app_name, account_username, account_password):
        
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
    def display_credentials(cls):
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
    def display_credentials(cls,):
        '''
        Method that returns the credential list
        '''
        return Credentials.credentials_list

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
    
    @classmethod
    def find_by_app_name(cls, app_name):
        '''
        This method takes in the application details and returns an individual's details.
        '''
        for credential in Credentials.credentials_list:
            if credential.app_name == app_name:
                return credential
        
    @staticmethod
    def generate_password(passwordlength):
        random_alphanumeric = string.ascii_letters + string.digits
        password = ''.join((random.choice(random_alphanumeric) for i in range (passwordlength)))
        return password