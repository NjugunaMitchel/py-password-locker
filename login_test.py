import unittest

from login import accounts 

###
class  AccountsTest(unittest.TestCase):
     def setup(self):
         self.accounts = accounts('Testuser','62552gdh','tester@gh.ck')

     def test_init(self):
         self.assertEqual(self.accounts.username,'Testuser')
         self.assertEqual(self.accounts.password,'62552gdh')
         self.assertEqual(self.accounts.email,'tester@gh.ck')
 
     def tearDown(self):
        accounts.user_list = []

     def test_auth_user(self):
        self.newAccount.saveAccounts()
        tester = accounts('Tester','uSjjfjf637','tester@ab.com')
        match_credentials = accounts.auth_by_email('tester@ab.com')
        tester.saveAccounts()
        self.assertEqual(match_credentials.email,tester.email)

     def  test_account_exists(self):
         test = accounts('Test','ddkke73883','test@co.com')
         test.saveAccounts()
         account_exists = accounts.account_exists(accounts,'test@co.com')
         self.assertTrue(account_exists)

     def test_display_all_Users(self):
        self.assertEqual(accounts.display_all_Users(),accounts.user_list)


if __name__ == '__main__':
    unittest.main()

