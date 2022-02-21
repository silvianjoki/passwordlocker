import random
import string

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

g



















def main ():
    print ('Hello, welcome to passwordlocker!')
    while True: 
        print ('Hello, welcome to passwordlocker!')
        print('\n')
        
        if short_code == 'nu':
            print('create username')
            created_user_name = input ()
            
            print ('create password')
            created_user_password = input()
            
            print ('confirm your password')
            confirm_password = input()
            
            while confirm_password != created_user_password:
                print('your passwords did not match try again!')
                print ('enter your password again')
                created_user_password= input()
                print ('confirm your password')
                confirm_password = input()
            else:
                print (f'congrats {created_user_name} account creation was a success! ')
                print('\n')
                print('proceed to login now')
                print(created_user_name)
                entered_username = input()
                print('your password please')
                entered_password = input()
                
            while entered_username != created_user_name or entered_password != created_user_password:
                print('your username or password did not match')
                print('username')
                entered_username = input()
                print ('password')
                entered_password = input()
            else: 
                print(f'welcome {created_user_name} you can now use your account! ')
                print ('\n')
                
        elif short_code == 'log':
            print('welcome')
            print ('share your user name ')
            default_user_name = input()
            
            print ('enter your password')
            default_user_password = input()
            print('\n')
            while default_user_name != 'sampleuser' or default_user_password != '12345':
                print('wrong username or password.')
                print ('enter user name')
                default_user_name = input()
                
                print('enter password')
                default_user_password = input()
                print ('\n')
            else: 
                print('login succesfull')
                print('\n')
                
        elif short_code == 'ex':
            break
        else: 
            print('insert a valid code for you to continue')
            
if __name__ == ' __main___ ':
    main()