import unittest

from login import accounts 

###
class  AccountsTest(unittest.TestCase):
     def setup(self):
         self.newAccount = accounts('Testuser','62552gdh','tester@gh.ck')

     def test_init(self):
         self.assertEqual(self.newAccount.username,'Testuser')
         self.assertEqual(self.newAccount.password,'62552gdh')
         self.assertEqual(self.newAccount.email,'tester@gh.ck')

     def tearDown(self):
        accounts.user_list = []

     def test_auth_user(self):
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
        self.assertEqual(accounts.display_accounts(accounts),accounts.user_list)


if __name__ == '__main__':
    unittest.main()

