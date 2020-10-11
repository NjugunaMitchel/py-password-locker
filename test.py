import unittest #importing the test module
#import Users class
from passwords import Credentials 
from passwords import accounts

## create a subclass 
class CredentialsTest(unittest.TestCase):
   
    '''
    Testing class that defines test cases
    '''
    def setUp(self):
        '''
        setUp runs before testcase'
        '''

        self.newCredentials = Credentials('MITCHEL','MUTHONI','NJUGUNAS','YHS67','ABC@CD.EF')

    def test_init(self):
        self.assertEqual(self.newCredentials.Fname,'MITCHEL')
        self.assertEqual(self.newCredentials.Sname,'MUTHONI')
        self.assertEqual(self.newCredentials.username,'NJUGUNAS')
        self.assertEqual(self.newCredentials.password,'YHS67')
        self.assertEqual(self.newCredentials.email,'ABC@CD.EF')

    def tearDown(self):
         Credentials.credentials_list = []

        # save a user
    def test_saveCredentials(self):
        self.newCredentials.saveCredentials()
        self.assertEqual(len(Credentials.credentials_list),1)

        #save multiple users
    def  test_savemore(self):
        self.newCredentials.saveCredentials()
        test = Credentials('jane','Doe','jadoe','djdj9','jd@jfj.vom')
        test.saveCredentials()
        self.assertEqual(len(Credentials.credentials_list),2)

        # delete user
    def test_delete(self):
        self.newCredentials.saveCredentials()
        test = Credentials('John','Doe','JD','ddduu773','john@ab.com')
        test.saveCredentials()
        self.newCredentials.delete()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_auth_user(self):
        self.accounts.saveCredentials()
        test = account('Mj','gsys728','melisa@k0.com')
        test.saveCredentials()
        match_credentials = accounts.auth_by_email('melisa@k0.com')
        self.assertEqual(match_credentials.email,test.email)


    def  test_account_exists(self):
         self.newCredentials.saveCredentials()
         test = accounts('tester','hdheu866','tester@co.com')
         test.saveCredentials()
         account_exists = accounts.account_exists('tester@co.com')
         self.assertTrue(account_exists)

    def test_display_all_Users(self):
        self.assertEqual(accounts.display_accounts(cls),accounts.user_list)
          
   


    

if __name__ == '__main__':
    unittest.main()


