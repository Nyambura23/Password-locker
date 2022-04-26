import unittest # Importing the unittest module
from contact import Account, Contact # Importing the account class
import pyperclip

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Mary","1234") # create account object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.name,"Mary")
        self.assertEqual(self.new_account.password,"1234")
        

    def test_save_user(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.user_list),1)

    def test_save_multiple_account(self):
          '''
          test_save_multiple_accountto check if we can save multiple account
          objects to our account_list
          '''
          self.new_account.save_account()
          test_account = Account("Test","user") # new account
          test_account.save_account()
          self.assertEqual(len(Account.account_list),2)
   
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

# other test cases here
    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user") # new account
            test_account.save_contact()
            self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0712345678") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting an account object
            self.assertEqual(len(Account.account_list),1)

    def test_find_contact_by_number(self):
        '''
        test to check if we can find an account by number and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0712345678") # new account
        test_account.save_account()

        found_account = Account.find_by_number("0712345678")

        self.assertEqual(found_account.number,test_account.number)

def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0712345678") # new account
        test_account.save_account()

        account_exists = Account.account_exist("Test")

        self.assertTrue(account_exists)

def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(Account.display_accounts(),Account.account_list)

def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from a found account
        '''

        self.new_account.save_account()
        Account.copy_password("user")

        self.assertEqual(self.new_account.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
