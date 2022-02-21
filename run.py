import random
import string

def main ():
    
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
                print(username)
                entered_username = input()
                print('your password please')
                entered_password = input()
                
            while entered_username != created_user_name or entered_password != created_user_password: