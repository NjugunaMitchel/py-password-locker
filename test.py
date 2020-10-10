import unittest #importing the test module
#import Users class
from passwords import User 

## create a subclass 
class UserTest(unittest.TestCase):
    '''
    Testing class that defines test cases
    '''
    def setUp(self):
        '''
        set up runs befors each test case
        '''

        self.Users = User('MITCHEL','MUTHONI','NJUGUNAS','YHS67','ABC@CD.EF')

    def test_init(self):
        self.assertEqual(self.Users.Fname,'MITCHEL')
        self.assertEqual(self.Users.Sname,'MUTHONI')
        self.assertEqual(self.Users.username,'NJUGUNAS')
        self.assertEqual(self.Users.password,'YHS67')
        self.assertEqual(self.Users.email,'ABC@CD.EF')

    def test_saveUser(self):
        self.Users.saveUser()
        self.assertEqual(len(User.user_list),1)

    def test_delete(self):
        self.Users.delete()
        selft.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()


