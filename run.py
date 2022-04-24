#!/usr/bin/env python3

from contact import Account

def create_account(name,password):
    '''
    Function to create a new account
    '''
    new_account = Account(name,password)
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

def find_account(name):
    '''
    Function that finds a account by name and returns the account
    '''
    return Account.find_by_name(name)

def check_existing_accounts(name):
    '''
    Function that check if a contact exists with that name and return a Boolean
    '''
    return Account.account_exist(name)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()

def check_copy_password(name):
    '''
    method that copies returned account's password to clipboard
    '''
    Account.copy_password(name)

def main():
    print("Hello Welcome to your Password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new account, dc - display accounts, fc -find an account, ex -exit the account list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Account")
                    print("-"*10)

                    print ("Account Name ....")
                    name = input()

                    print("Password ...")
                    password = input()

    
                    save_accounts(create_account(name,password)) # create and save new account.
                    print ('\n')
                    print(f"New Account {name} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_accounts():
                            print("Here is a list of all your accounts")
                            print('\n')

                            for account in display_accounts():
                                    print(f"{account.name} {account.password}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any accounts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the name you want to search for")

                    search_name = input()
                    if check_existing_accounts(search_name):
                            search_account = find_account(search_name)
                            print(f"{search_account.name}")
                            print('-' * 20)

                            print(f"name.......{search_account.name}")
                            
                    else:
                            print("That account does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()