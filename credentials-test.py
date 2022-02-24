'''
App lock test module
'''
import unittest 
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    This test case defines Credential test cases
    
    Args:
    unittest.Tescase: class helps create test cases 
    '''
    
    def setUp(self):
        '''
        This sets up a method to run before each test case
        '''
        #create credentials object
        self.new_credentials = Credentials('Silvia', 'insta', 'insta1')
        
    def tearDown(self):
        '''
        teardown method conducts a clean up after each test is run
        '''
        Credentials.credentials_list = []
        
    def test_init(self):
        '''
        Tests whether the object is initialized
        '''
        self.assertEqual( self.new_credentials.app_name, 'Silvia')
        self.assertEqual( self.new_credentials.account_username, 'insta')
        self.assertEqual (self.new_credentials.account_password, 'insta1')
        
    def test_save_credential(self):
        '''
        Test case confirms whether user object is saved into the list
        '''
        #save new credential
        self.new_credentials.save_credentials()
        
        self.assertEqual(len (Credentials.credentials_list), 1)
        
    def test_save_multiple_credentials(self):
        '''
        Test case to save multiple objects
        '''
        #save new information for multiple users
        self.new_credentials.save_credentials()
        
        test_credentials = Credentials('silvie', 'Twitter', 'twitter1')
        
        test_credentials.save_credentials()
        
        self.assertEqual( len (Credentials.credentials_list),2)
        
    def test_generate_password(self):
        '''
        Test case to check whether user can sign into the app
        '''
        generate_password = self.new_credentials.generate_password()
        
        self.assertEqual(len (generate_password), 8)
        
    def test_show_credentials(self):
        '''
        Test case displays all user credentials
        '''
        self.new_credentials.save_credentials()
        
        test_credentials = Credentials('silvie', 'Twitter', 'twitter1')
        
        test_credentials.save_credentials()
        
        test_credentials = Credentials ('silvie', 'Twitter', 'twitter1')
        
        test_credentials.save_credentials()
        
        self.assertEqual(len (Credentials.display_credentials ('silvie')), 2)
        
    def test_credentials_exist(self):
        #save the new credential
        self.new_credentials.save_credentials()
        
        test_credential = Credentials ('silvie', 'Twitter', 'twitter1')
        
        test_credential.save_credentials()
        
        #user contacts exist method
        credentials_exists = Credentials.credentials_exist('Twitter')
        
        self.assertTrue(credentials_exists)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)