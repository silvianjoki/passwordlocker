import code
from unicodedata import name
from user import User
from credentials import Credentials


def create_user(username, password):
    '''
    this function creates a new user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    Function to save user information
    '''
    user.save_user()

def remove_user(user):
    '''
    Function removes the user
    '''
    user.delete_user()

def check_existing_user(username, password):
    '''
    Function to define existing user authentication
    '''
    return User.user_exists(username, password)

def find_user(username):
    '''
    Function finds user by username
    '''
    return User.find_by_username(username)

def create_credentials (app_name, account_username, account_password):
    '''
    Function enables addition of new credentials
    '''
    new_credentials = Credentials(app_name, account_username, account_password)
    return new_credentials

def check_existing_user(username, password):
    '''
    Function checks for existing users
    '''
    return User.user_exists(username, password)

def display_credentials():
    '''
    Function displays the saved credentials
    '''
    return Credentials.display_credentials()

def remove_credentials(new_credentials):
    '''
    Function to remove credentials
    '''
    new_credentials.delete_credentials()

def find_credentials(app_name):
    '''
    function uses app_name to find credentials of users
    '''
    return Credentials.find_by_app_name(app_name)

def check_existing_credentials(app_name):
    '''
    Function checks existing credentials by linking to the application name
    '''
    return Credentials.credentials_exist(app_name)
    
def save_credentials (new_credentials):
    '''
    Function to save credentials
    '''
    new_credentials.save_credentials()
    
def generated_password(username):
    '''
    Function that generates random password of 8 characters
    Args:
    account: takes account name 
    '''
    password = Credentials.generate_password()
    return password



def main ():
    print ('Hello, welcome to passwordlocker! Kindly share your name')
    username = input()
    print('Hello, explore this application.')
    
    while True:
        '''
        Application control loop
        '''
        print('''Short codes
        nu- new user short code to create account
        lg- log in to your password locker account
        ex- exit password locker account''')
        short_code = input().lower()
        
        if short_code == 'nu':
            print ('\n Create new account here')
            print ('new passwordlocker account')
            print('_'*10)
            print('username ..')
            username = input()
            
            print('input password for your account')
            password = input()
            
            save_user(create_user(username, password))
            print('Hi, your account has been successfully created')
        

        
        elif short_code =='lg':
            print ('_'*20)
            print('log in into the passwordlocker account')
            print('enter your username')
            username = input()
            print('password')
            password = input()
            print('\n')
            
            if check_existing_user(username, password) == None:
                print('if account exists try again, if not create a new account')
            else:
                check_existing_user(username, password)
                print('\n succesful login')
                while True:
                    print('use short codes to navigate to what you want to do.\n cc: Create new credentials \n dc: delete a credential \n fc: Find credentials \n vc: View all credentials \n ex: Exit the app')
                    short_code = input().lower()
                    
                    if short_code == 'cc':
                        print('\n Create new credentials')
                        print('_'*10)
                        
                        print('Application name:')
                        app_name = input()
                        
                        print('Account username:')
                        account_username = input()
                        
                        print('Account password:')
                        account_password = input()
                        
                        save_credentials(create_credentials(app_name, account_username, account_password))
                        print('Account credentials under you name were created ')
                        continue
                    
                    elif short_code == 'dc':
                        '''delete existing credentials'''
                        print('Kindly add details for the account you wish to delete')
                        print('*'*10)
                        app_name = input()
                        print('this will delete details for ex shared above')
                        remove_credentials(find_credentials(app_name))
                        print('Your credentials were successfully removed' )
                    
                    
                    elif short_code == 'vc':
                        '''display class credentials'''
                        if display_credentials():
                            print('View your account credentials')
                            print('*'*10)
                            
                            for credential in display_credentials():
                                print(f'App name: {credential.app_name}' )
                                print(f'Account_username: {credential.account_username}')
                                print(f'Account_password: {credential.account_password}')
                                print('*'*10)
                                
                        else: 
                            print('No existing credentials here')
                            continue


                    elif short_code == 'fc':
                        '''find credentials for user'''
                        print('find your credenetials in the list')
                        print('_'*10)
                        print('\eg Insta')
                        searched_app = input()
                        
                        if check_existing_credentials(searched_app):
                            searched_credential = find_credentials(searched_app)
                            print(f'app_name {searched_credential.app_name}')
                            print(f'account_username {searched_credential.account_username}')
                            print(f'account_password {searched_credential.account_password}')
                            
                        else:
                            print('Sadly, we coud not find the' + {searched_credential} + 'credentials')
                        continue

                    elif short_code == 'ex':
                        '''exit the app'''
                        print(' thank you for visiting our application ')
                        print('*'*10)
                    else:
                        print(' kindly input a code to navigate to your credentials or add them again.')
                        continue

                    
        elif short_code == 'ex':
            print('Thanks for stopping by.')
            break
        else:
            print('did you add anything?Kindy try againg')

if __name__ == '__main__':
    main()