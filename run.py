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
                print('\n')
                print("CA -or VA")
                choose= input()
                print('\n')
                if choose == "CA":
                    print("Add your account")
                    print('\n')
                    accountusername=loginUsername
                    print("Account name")
                    accountname=input()
                    print('\n')
                    print("Autogenerate password (A) or create custom password (C)")
                    decision=input()
                    if decision== "A":
                        characters=string.ascii_letters+string.digits
                        accountpassword="".join(random.choice(characters)for x in range(random.randint(6,16)))
                        print(f"Password: {accountpassword}")
                    elif decision== "C":
                        print("Enter password")
                        accountpassword=input()
                    else:
                        print("Kindly select a valid choice")
                        save_accounts(create_account(accountname,accountusername,accountpassword))
                        print('\n')
                        print(f"Username: {accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}")
                elif choose== "VA":
                    if find_account(accountusername):
                        print("Here are all your accounts:")
                        print('\n')
                        for user in display_accounts():
                            print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")
                    else:
                        print("Invalid credentials")
                        print('\n')
                else:
                    print("Please try again")
                    print('\n')
            else:
                print("The info you provided is not correct")
                print('\n')
        else:
            print("Please select a valid option")
            print('\n')

if __name__ == '__main__':
    main()