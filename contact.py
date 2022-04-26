import pyperclip

class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty user list

    def __init__(self,name,username, password):

      # docstring removed for simplicity

        self.name = name
        self.username = username
        self.password = password

       

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns an user that matches that number.

        Args:
            number: number to search for
        Returns :
            User of person that matches the number.
        '''

        for user in cls.user_list:
            if user.password == number:
                return user

    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.name == number:
                    return True

        return False


    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_password(cls,number):
        account_found = User.find_by_number(number)
        pyperclip.copy(account_found.password)

class Credentials:
    """
    Class that generates new instances of credentials.
    """

    accounts= [] # Empty account list

    def __init__(self,accountname,accountusername, accountpassword):

      # docstring removed for simplicity

        self.accountname = accountname
        self.accountusername = accountusername
        self.accountpassword = accountpassword

       

    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Credentials.accounts.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Credentials.accounts.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns an account that matches that number.

        Args:
            number: number to search for
        Returns :
            Account of person that matches the number.
        '''

        for account in cls.accounts:
            if account.accountusername == number:
                return account

    def account_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.accounts:
            if account.name == number:
                    return True

        return False


    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.accounts


    @classmethod
    def copy_password(cls,number):
        account_found = Credentials.find_by_number(number)
        pyperclip.copy(account_found.password)

