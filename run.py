#!/usr/bin/env python3
from optparse import Option
import string
import random
from contact import User
from contact import Credentials

def create_user(name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(name,username,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a account by number and returns the account
    '''
    return User.find_by_number(number)

def check_existing_users(name):
    '''
    Function that check if a userexists with that name and return a Boolean
    '''
    return User.user_exist(name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def check_copy_password(name):
    '''
    method that copies returned user's password to clipboard
    '''
    User.copy_password(name)

def create_account(accountname,accountusername,accountpassword):
    '''
    Function to create a new account
    '''
    new_account = Credentials(accountname,accountusername,accountpassword)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()

def find_account(number):
    '''
    Function that finds a account by number and returns the account
    '''
    return Credentials.find_by_number(number)

def check_existing_accounts(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credentials.account_exist(name)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()

def check_copy_password(name):
    '''
    method that copies returned account's password to clipboard
    '''
    Credentials.copy_password(name)

def main():
    # while True:
        print ("Hi.Welcome to Password Locker,Select the short_cord to navigate through:.")
        print('\n')
        print('to create new user use "NU":')
        print('\n')
        print('to login use "LG"')
        option=input()
        if option == "NU":
            print("Enter your name...")
            name=input()
            print("Enter your username...")
            username=input()
            print("Enter your password...")
            password=input()
            save_users(create_user(name,username,password))
            print("Your account was succesfully created.Here are the details;")
            print('\n')
            print(f"Name: {name} \nUsername: {username} \nPassword {password}")
            print("\nKindly login using your details")
            print('\n')

        elif option =="LG":
            print("Username...")
            loginUsername=input()
            print("Password...")
            loginPassword=input()
            if find_user(loginPassword):
                print('\n')
                print("You can either create mutiple account (CA) or view existing accounts (VA)")
                
            
    
# def main():
#     print('Hi.Welcome to Password Locker.')
#     print('\n')
#     print('Select the short_cord to navigate through:')
#     print('\n')
#     print('to create new user use "NU":')
#     print('\n')
#     print('to login use "LG" or "Ex" to exit')
#     print('\n')
#     print('to delete Account use "DU"')
#     short_code = input().lower()
#     if short_code == 'nu':
#         print('Enter new account details')
#         print('\n')
#         username = input('Enter Username: ')
#         while True:
#             print('CP = to create password')
#             password_choice = input().lower()
#             if password_choice == 'cp':
#                 password = input('Confirm Password: ')
#                 print('\n')

#             else:
#                 print('Invalid password. Try again')
#             save_users(create_user(username, password))

#         print('\n')
#         print(
#             f'Welcome {username} to your account')
#         print('\n')

#     elif short_code == 'lg':
#         print('Enter Your Account Username and Password to Login')
#         username = input('Username:')
#         password = input('Password:')
#         check_user = find_user(username, password)
#         if find_user == check_user:
#             print(f'Welcome back {username}')
#             print('\n')

#         elif short_code == 'du':
#             print('Are you sure want to delete Account??? If YES,type')
#             username = input('Username :')
#             password = input('Password:')
#             check_user = find_user(username, password)
#             if find_user == check_user:
#                 print(f'Account {username} has been successfully deleted ')
#                 print('\n')

#             else:
#                 print('Incorrect account name')
#                 print('\n')


#         elif short_code == 'ex':
#             print('We are Sorry to see you leave!!!!')
#             print('\n')

#         else:
#             print('Invalid Pasword. Try again!')
#             print('\n')


# def main():
#     print("Hello Welcome to your Password locker. What is your name?")
#     user_name = input()

#     print(f"Hello {user_name}. what would you like to do?")
#     print('\n')

#     while True:
#             print("Use these short codes : cc - create a new account, dc - display accounts, fc -find an account, ex -exit the account list ")

#             short_code = input().lower()

#             if short_code == 'cc':
#                     print("New Account")
#                     print("-"*10)

#                     print ("Account Name ....")
#                     name = input()

#                     print("Password ...")
#                     password = input()

    
#                     save_accounts(create_account(name,password)) # create and save new account.
#                     print ('\n')
#                     print(f"New Account {name} created")
#                     print ('\n')

#             elif short_code == 'dc':

#                     if display_accounts():
#                             print("Here is a list of all your accounts")
#                             print('\n')

#                             for account in display_accounts():
#                                     print(f"{account.name} {account.password}")

#                             print('\n')
#                     else:
#                             print('\n')
#                             print("You dont seem to have any accounts saved yet")
#                             print('\n')

#             elif short_code == 'fc':

#                     print("Enter the name you want to search for")

#                     search_name = input()
#                     if check_existing_accounts(search_name):
#                             search_account = find_account(search_name)
#                             print(f"{search_account.name}")
#                             print('-' * 20)

#                             print(f"name.......{search_account.name}")
                            
#                     else:
#                             print("That account does not exist")

#             elif short_code == "ex":
#                     print("Bye .......")
#                     break
#             else:
#                     print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()