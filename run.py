#!/usr/bin/env python3.8
from passwords import Credentials
from login import accounts
import random
#create credentials func
def create(fname,lname,user,passwords,email):
    newCredentials = Credentials(fname,lname,user,passwords,email)
    return newCredentials

#delete
'''
function to delete credentials & accounts
'''
def delete(credentials):
    credentials.delete()

def deleteAccount(accounts):
    accounts.deleteAccount()


'''
save credentials & accounts
'''
def saveCredentials(Credentials):
    Credentials.saveCredentials()

def saveAccounts(accounts):
    accounts.saveAccounts()


'''
search credentials
'''
def auth_user(email):
    return Credentials.auth_by_email

'''
check if contact exist
'''
def account_exists(email):
    return Credentials.accounts_display(email)


'''
display
'''
def display_all_users():
    return accounts.display_all_users


def main():
    print('Your name?')
    username = input()
    code = input(f'Press Enter {username}')
    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list,del-to delete ")

        short_code = input()
        if short_code == 'cc':
            print('First name:')
            fname = input()

            print('last name:')
            lname = input()

            print('username')
            username = input()

            print('email:')
            email = input()

            print('password:')
            passwords = input(round(random.random()))


            saveCredentials(create(fname,lname,username,passwords,email))
            print('/n')
            print(f'new Credentials{fname}')

        elif short_code == 'dc':
            if display_all_users():
                print('users:')
                for account in display_all_users():
                    print(f'{Credentials.username} {Credentials.email}')

        elif short_code == 'fc':
            print('enter email address to search')
            search = input()
            if accounts_exists(email):
                auth_by_email = find_contact(search)

                print(f'{search.first}')

            else:
                print('NO credentials found!')

        elif short_code == 'del':
            print('input Y confirm')
            confirm = input()
            if delete():
                credentials.delete()
                print('credential deleted')

            else:
                print('credentials not found')



        elif short_code == 'ex':
            print('happy coding!')
            break

        else:
            print('Not an existing shortcut')


if __name__ == '__main__':
    main()


