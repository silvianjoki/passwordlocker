from collections import UserList
from signal import default_int_handler

import unittest  #importing the unittesting module
from user import User, user


class Testuser(unittest.TestCase):
    '''
    this test class defines the test cases for the user class 
    '''
    '''
    Args:
    unittest.Testcase: testcase class which helps in creating test cases.
    '''
    
    def setUp(self):
        '''
        Setup method to run before each test case. 
        '''
        self.new_user = user('Silvia, 53')
        
    def test_initialization(self):
        '''
        test_init test case to test if the object is initialized appropriately
        '''
        self.assertEqual(self.new_user.username, 'Silvia')
        self.assertEqual(self.new_user.password, '53')
        
    def test_save_user(self):
        '''
        test_save-user test case to test if the contact object is added into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
        
    def tearDown(self):
        '''
        tearDown method conducts a clean up once each test case has run
        '''
        user.user_list = []
        
    def test_user_exists(self):
            
        '''
        will test whether the user exists within the user list
        '''
        self.new_user.save_user()
        test_user = User('future', '68')
        test_user.save_user()
        
        user_exists = User.user_exists('future', '68')
        self.assertTrue(user_exists)

    def test_delete_user(self):
        '''
        test_delete_user method ensures a deleted user is removed from the user list 
        '''
        self.new_user.save_user()
        test_user = User('Test', '76')
        test_user.save_user()
        
        test_user.delete_user()
        self.assertEqual(len(User.user_list,1))
        
    def test_find_user_by_username(self):
        '''
        test to check whether one can find user by username
        '''
        self.new_user.save_user()
        test_userA = User('testy', '54')
        test_userA.save_user()
        
        found_user = User.find_by_username('testy')
        self.assertEqual(found_user.password, test_userA.password)
    
if __name__ == '__main__':
    unittest.main()