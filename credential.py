import random
import string

class Credential: 
    
    # creates new credentials for users
    
    credential_list = []
    
    def __init__(self, application , account_username, account_password) -> None:
        
        self.application = application
        self.account_username = account_username
        self.account_password = account_password
        