'''
App lock test module
'''
import unittest 
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
    This test case defines Credential test cases
    
    Args:
    unittest.Tescase: class helps create test cases 
    '''
    
    def setUp(self):
        '''
        This sets up a method to run before each test case
        '''
        #create credential object
        self.new_credential = Credential('Silvia', 'insta', 'insta1')
        
    def tearDown(self):
        '''
        teardown method conducts a clean up after each test is run
        '''
        Credential.credential_list = []
        
    def test_init(self):
        '''
        Tests whether the object is initialized
        '''
        self.assertEqual( self.new_credential.user_password, 'Silvia')
        self.assertEqual( self.new_credential.credential_name, 'insta')
        self.assertEqual( self.new_credential.credential_password, 'insta1')
        
    def test_save_credential(self):
        '''
        Test case confirms whether user object is saved into the list
        '''
        #save new credential
        self.new_credential.save_credential()
        
        self.assertEqual(len (Credential.credential_list), 1)
        
    def test_save_multiple_credential(self):
        '''
        Test case to save multiple objects
        '''
        #save new information for multiple users
        self.new_credential.save_credential()
        
        test_credential = Credential('silvie', 'Twitter', 'twitter1')
        
        test_credential.save_credential()
        
        self.assertEqual( len (Credential.credential_list),2)
        
    def test_generate_password(self):
        '''
        Test case to check whether user can sign into the app
        '''
        generate_password = self.new_credential.generate_password()
        
        self.assertEqual(len (generate_password), 8)
        
    def test_show_credential(self):
        '''
        Test case displays all user credentials
        '''
        self.new_credential.save_credential()
        
        test_credential = Credential('silvie', 'Twitter', 'twitter1')
        
        test_credential.save_credential()
        
        test_credential = Credential ('silvie', 'Twitter', 'twitter1')
        
        test_credential.save_credential()
        
        self.assertEqual(len (Credential.display_credentials ('silvie')), 2)
        
    def test_credential_exist(self):
        #save the new credential
        self.new_credential.save_credential()
        
        test_credential = Credential ('silvie', 'Twitter', 'twitter1')
        
        test_credential.save_credential()
        
        #user contacts exist method
        credential_exists = Credential.credential_exist('Twitter')
        
        self.assertTrue(credential_exists)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)