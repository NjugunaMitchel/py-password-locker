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

