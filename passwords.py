class Credentials():

# users list
  credentials_list  = []

  '''
  initialize a class
  '''
  def __init__(self,Fname,Sname,username,password,email):
      '''
      users class 'blueprint'
      '''
      self.Fname = Fname
      self.Sname = Sname
      self.username = username
      self.password = password
      self.email = email 

  def saveCredentials(self):
        Credentials.credentials_list.append(self)


  def delete(self):
        Credentials.credentials_list.remove(self)

class accounts(Credentials):
    user_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

@classmethod
def auth_by_email(cls,email):
    for accounts in cls.user_list:
        if accounts.email == email:
            return accounts

def  account_exists(cls,number):
    for accounts in cls.user_list:
        if accounts.email == email:
            return true

    return false;






""" def authn_user(self):
        details = input('your name') """
      