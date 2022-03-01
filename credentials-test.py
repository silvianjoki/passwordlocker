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
        self.new_credentials = Credentials('insta', 'silvia', 'insta1')
        
    def tearDown(self):
        '''
        teardown method conducts a clean up after each test is run
        '''
        Credentials.credentials_list = []
        
    def test_init(self):
        '''
        Tests whether the object is initialized
        '''
        self.assertEqual( self.new_credentials.app_name, 'insta')
        self.assertEqual( self.new_credentials.account_username, 'silvia')
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
        test_credentials = Credentials('Twitter','silvie' 'twitter1')
        test_credentials.save_credentials()
        self.assertEqual( len(Credentials.credentials_list), 2)
        
    def test_generate_password(self):
        '''
        Test case to check whether user can sign into the app
        '''
        generated_password = self.new_credentials.generate_password()
        self.assertEqual( len(generated_password), 8 )
        
    def test_display_credentials(self):
        '''
        Test case displays all user credentials
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
        
        
    def test_find_by_application_name(self):
        '''
        test to check if we can find a credentials by application name
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Insta", "Gamie", "101")
        test_credentials.save_credentials()
        
        found_credentials = Credentials.find_by_app_name("Insta")
        self.assertEqual(found_credentials.account_username, test_credentials.account_username)
        
    
    def test_credentials_exist(self):
        #save the new credential
        self.new_credentials.save_credentials()
        test_credential = Credentials ( 'Twitter', 'silvie', 'twitter1')
        test_credential.save_credentials()
        credentials_exists = Credentials.credentials_exist('Twitter')
        self.assertTrue(credentials_exists)
        
if __name__ == '__main__':
    unittest.main()