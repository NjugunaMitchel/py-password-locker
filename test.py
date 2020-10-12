import unittest #importing the test module
#import Users class

from passwords import Credentials

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

   


  
          
   


    

if __name__ == '__main__':
    unittest.main()


