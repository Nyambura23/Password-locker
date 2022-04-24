import pyperclip

class Account:
    """
    Class that generates new instances of accounts.
    """

    account_list = [] # Empty account list

    def __init__(self,name, password):

      # docstring removed for simplicity

        self.name = name
        self.password = password
       

    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns an account that matches that name.

        Args:
            name: name to search for
        Returns :
            Account of person that matches the name.
        '''

        for account in cls.account_list:
            if account.phone_name == name:
                return account

    def account_exist(cls,name):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.account_list:
            if account.name == name:
                    return True

        return False


    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    @classmethod
    def copy_password(cls,name):
        account_found = Account.find_by_name(name)
        pyperclip.copy(account_found.password)

