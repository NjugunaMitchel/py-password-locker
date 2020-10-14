class accounts:
    user_list = []

    def __init__(self,username,password,email):
        self.accounts.username = username
        self.accounts.password = password

    def saveAccounts(self):
        accounts.user_list.append(self)

    def deleteAccount(self):
        accounts.user_list.remove(self)

    @classmethod
    def auth_by_email(cls,email):
        for account in cls.user_list:
            if account.email == email:
                return account

    def  account_exists(cls,email):
        for accounts in cls.user_list:
            if accounts.email == email:
                return True

        return False;

    def display_all_users(cls):
        return cls.user_list