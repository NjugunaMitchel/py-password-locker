#!/usr/bin/env python3.8
from passwords import Credentials
import random
#create credentials func
def create(fname,lname,user,passwords,email):
    newCredentials = Credentials(fname,lname,user,passwords,email
    return newCredentials

#delete
'''
function to delete credentials
'''
def delete(credentials):
    credentials.delete()


'''
save credentials
'''
def saveCredentials(Credentials):
    Credentials.saveCredentials()


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
    return Credentials.display_all_users


def main():
    username = print('Your name?')
    code = input(f'would you like to create an account {username}')
    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")



        if code ==  'Y':
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
                passwords = input(print(random.random()))


                saveCredentials(create(fname,lname,user,passwords,email))
                print('/n')
                print(f'new Credentials{fname}')

        elif short_code == 'dc':
            if display_all_users():
                print('users:')
                for credentials in display_all_users():
                    print(f'{Credentials.username} {Credentials.email}'')

        elif short_code == 'fc':
            print('enter email address to search')
            search = input()
            if accounts_exists(email):
                auth_by_email = find_contact(search)

                print(f'{search.first}')

            else:
                print('NO credentials found!')

        elif short_code == 'ex':
            print('happy coding!')
            break

        else:
            print('Not an existing shortcut')


if __name__ == '__main__':
    main()


