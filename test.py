import unittest #importing the test module
#import Users class
from passwords import User 

## create a subclass 
class UserTest(unittest.TestCase):
    '''
    Testing class that defines test cases
    '''
    def tearDown(self):
       """  '''
        set up runs befors each test case
        '''

        self.Users = User('MITCHEL','MUTHONI','NJUGUNAS','YHS67','ABC@CD.EF')

    def test_init(self):
        self.assertEqual(self.Users.Fname,'MITCHEL')
        self.assertEqual(self.Users.Sname,'MUTHONI')
        self.assertEqual(self.Users.username,'NJUGUNAS')
        self.assertEqual(self.Users.password,'YHS67')
        self.assertEqual(self.Users.email,'ABC@CD.EF') """
    User.user_list = []

        # save a user

    def test_saveUser(self):
        self.Users.saveUser()
        self.assertEqual(len(User.user_list),1)

        #save multiple users
    def  test_savemore(self):
        self.User.saveUser()
        test = User('jane','Doe','jadoe','djdj9','jd@jfj.vom')
        test.save()
        self.assertEqual(len(User.user_list),2)

        # delete user
    def test_delete(self):
        self.Users.saveUser()
        test = User('John','Doe','JD','ddduu773','john@ab.com')
        test.saveUser()
        self.Users.delete()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()


