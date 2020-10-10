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
        setUp runs before testcase'
        '''

        self.newUser = User('MITCHEL','MUTHONI','NJUGUNAS','YHS67','ABC@CD.EF')

    def test_init(self):
        self.assertEqual(self.newUser.Fname,'MITCHEL')
        self.assertEqual(self.newUser.Sname,'MUTHONI')
        self.assertEqual(self.newUser.username,'NJUGUNAS')
        self.assertEqual(self.newUser.password,'YHS67')
        self.assertEqual(self.newUser.email,'ABC@CD.EF')

    def tearDown(self):
         User.user_list = []

        # save a user
    def test_saveUser(self):
        self.newUser.saveUser()
        self.assertEqual(len(User.user_list),1)

        #save multiple users
    def  test_savemore(self):
        self.newUser.saveUser()
        test = User('jane','Doe','jadoe','djdj9','jd@jfj.vom')
        test.saveUser()
        self.assertEqual(len(User.user_list),2)

        # delete user
    def test_delete(self):
        self.newUser.saveUser()
        test = User('John','Doe','JD','ddduu773','john@ab.com')
        test.saveUser()
        self.newUser.delete()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()


