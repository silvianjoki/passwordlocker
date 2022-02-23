from os import fchdir
from typing import Tuple
from xml.etree.ElementPath import find
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
    return User.user_exists(username)

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



def main ():
    '''
    Function that runs the password locker
    '''
    print ('Hello, welcome to passwordlocker! Use this short codes to get around')
    
    while True: 
        '''
        Loop that manages the whole application
        '''
        
        print('''Short codes
        nu- new user short code to create account
        lg- log in to your password locker account
        ad- add account details for a platform
        dl- delete account details for a platform 
        ex- exit password locker account''')
        
        #Get user short codes 
        short_code = input().lower()
        
        if short_code == 'nu':
            '''
            Create a new user account
            '''
            
            print ('\n')
            print ('new passwordlocker account')
            print('_'*10)
            
            print('username ..')
            user_name = input()
            
            print('password')
            login_password = input()
            #save new user 
            save_user(create_user(user_name, login_password))
            
            print('\n')
            # print(f'\n {user_name} welcome to passwordlocker')
            print('\n')
        
        elif short_code =='lg':
            print('\n')
            print('log in into the passwordlocker account')
            print('enter your username')
            username = input()
            
            print('enter your password')
            login_password= input()
            
            if check_existing_user(username, login_password):
                print('\n succesful login')
                print('use short codes to navigate to what you want to do CC: Create new credentials \n DC: delete a credential \n FC: Find credentials  \n VC: View all credentials')
                short_code = input().lower()
                
                if short_code == 'CC':
                    print('\n Create new credentials')
                    print('_'*10)
                    while True:
                        print('Application name:')
                        app_name = input()
                        if app_name !='':
                            # print(f'whats your user name for the app/desired name')
                            account_username = input()
                            
                            while True:
                                print(f"\nDo you have an existing password on {app_name}? Y/N?")
                                existing_password = input()
                                if existing_password =='Y':
                                    print(f"Insert your {app_name} password ")
                                    account_password = input()
                                    save_credentials(create_credentials(
                                        app_name, account_username, account_password))
                                    print(f'\n Account credentials for {app_name} under you name were created ')
                                    break
                                
                                elif existing_password == 'N':
                                    while True:
                                        print(f'enter your preffered password to use on {app_name} ')
                                        account_password = input()
                                        save_credentials(create_credentials(
                                            app_name, account_username, account_password))
                                        print (f'Account details for {app_name} were successfully created ')
                                        break
                                    
                                elif short_code == 'FC':
                                    print('\n find credentials')
                                    print('_'*10)
                                    print('\eg Instagram')
                                    searched_app = input()
                                    
                                    if check_existing_credentials(searched_app):
                                        searched_credential = find_credentials(searched_app)
                                        print(f'\n app-name: {searched_app.app_name}, \n {searched_credential.account_username}, \n password: {searched_credential.account_password} ')
                                        
                                    else:
                                        print(f'\Sadly, we could not find the {searched_app} credentials')
                                        
                                        continue
                                
                                elif short_code == 'DC':
                                    print(f'\n delete credentials')
                                    app_name= input()
                                    
                                    if check_existing_credentials(app_name):
                                        while True:
                                            print(f'you sure you wanna do that to your {app_name} Y/N ')
                                            delete_credential = input()
                                            if delete_credential == 'Y':
                                                remove_credentials(find_credentials(app_name))
                                                print(f'\n Your credentials were successfully removed for {app_name} ')
                                                
                                            elif delete_credential == 'N':
                                                print('\n your credentials have remained here. ')
                                                break
                                            else: 
                                                print('kindly select a valid option try again either Yes or No (Y/N')
                                                continue
                                    
                                    else:
                                        print(f'\n credentials for the {app_name} do not exist')
                                        continue
                                        
                                elif short_code == 'VC':
                                    display_credentials
                                    print('\n view all your credentials here')
                                    print('_'*10)
                                    for credential in display_credentials():
                                        print (f'\App name: {credential.app_name} \n Username: {credential.account_username}, \n Password: {credential.account_password} ')
                                        continue
                                    else:
                                        print('\n Kindly add your details to the lists')
                                        continue
                                    
                                elif short_code == 'ex':
                                    print(f'\n you successfully left the application')
                                
                                else:
                                    print('\n You did not select a valid option here')
                                    print('\n kindly try again')
                                    continue
                                
                        else:
                            print(f'\n did you add anything?')
                            
                            
                        break
                
                
if __name__ == ' __main___ ':
    main()