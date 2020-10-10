class User:

# users list
  user_list  = []

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

  def saveUser(self):
        User.user_list.append(self)

  def delete(self):
        User.user_list.remove(self)
      