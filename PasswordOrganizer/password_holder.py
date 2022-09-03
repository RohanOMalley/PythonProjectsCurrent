"""File: password_holder.py

   Author: Rohan O'Malley

   Purpose: The program creates User objects and stores them in
   the folder the same as this program. Each User holds accounts
   mapped to passwords and they can be changed at will. Program can
   find User in the folder to modify for later use or create new Users.
"""
import shelve, sys, os
from pathlib import Path

# ---------------------------------------------------------
class User:
    def __init__(self, name):
        self.current_user = name
        self.user_pass_dict = {}
    
    def add_account (self, account, username, password):
        if account in self.user_pass_dict:
            return False
        self.user_pass_dict[account] = [username, password]

    def change_pass (self, account, new_password):
        if account not in self.user_pass_dict:
            return False
        self.user_pass_dict[account][1] = new_password
        
    def change_user (self, account, new_username):
        if account not in self.user_pass_dict:
            return False
        self.user_pass_dict[account][0] = new_username

    def print_user (self):
        print('-' * 25, end='\n')
        print(f'Current User: {self.current_user}')
        print('-' * 25, end='\n')
        for acc in self.user_pass_dict:
            print('*' * 25, end='\n')
            print(f'Account Name:  {acc}')
            print(f'    Username: {self.user_pass_dict[acc][0]}')
            print(f'    Password: {self.user_pass_dict[acc][1]}')
            print('*' * 25, end='\n')
        print('-' * 25, end='\n')

# ----------------------------------------------------------




def add_accounts (cur_user):
    '''
    Used to add accounts to the current User passed in
    Can also display the accounts that User holds
    '''
    adding_accounts = True

    while adding_accounts is True:
        print('')
        acc_command = str(input(f'Add an Account to {cur_user.current_user}? (yes, no, list): '))
        print('')
        acc_command = acc_command.lower().strip()
        if acc_command == 'yes':
            account_name = str(input('Account Name? '))
            print('')
            username = str(input(f'Username for {account_name}? '))
            print('')
            password = str(input(f'Password for {account_name}? '))
            print('')
            cur_user.add_account( account_name, username, password )

        elif acc_command == 'list':
            cur_user.print_user()

        elif acc_command == 'no':
            change = True
            changeInfo(cur_user, change)
            adding_accounts = False

def changeInfo (cur_user, change):
    """
    Changes info in the User, can change the account with 
    the password associated with the account.
    """
    while change is True:
        cur_user.print_user()
        print('')
        do_change = str(input('Is this correct? '))
        print('')

        if do_change == 'no':
            acc_to_change = str(input('Account name to change? '))
            print('')
            user_or_pass = str(input('Username or Password change? '))
            print('')
            if user_or_pass == 'username':
                new_username = input(f'New Username for {acc_to_change} ')
                cur_user.change_user(acc_to_change, new_username)

            elif user_or_pass == 'password':
                acc_to_change = input('Account name to change? ')
                print('')
                new_pass = input(f'New Password for {acc_to_change}')
                print('')
                cur_user.change_pass(acc_to_change, new_pass)
        elif do_change == 'yes':
            change = False
                
def main():
    run = True

    while run is True:
        use_command = input('New User or Find a Current User or Done?\n')
        print('')
        use_command = use_command.lower().replace(' ','')

        if use_command == 'new':
            cur_name = str(input("User's Name (First and Last): "))
            print('')
            cur_name = cur_name.strip().replace(' ','').lower()
            cur_user = User(cur_name)

            add_accounts(cur_user)

            shelfSavePath = Path(sys.argv[0]).parent / Path(cur_user.current_user)
            user_file = shelve.open(f'{shelfSavePath}')
            user_file[f'{cur_user.current_user}'] = cur_user
            user_file.close()
            
        elif use_command == 'find':
            user_to_find = str(input("User's Name (First and Last): "))
            print('')
            
            user_to_find = user_to_find.strip().replace(' ','').lower()
            path = Path(f'/Users/rohanomalley/Documents/CSC 120/Password_org/{user_to_find}.db')

            if path.is_file() is True:
                shelfSavePath = Path(sys.argv[0]).parent / Path(user_to_find)
                user_file = shelve.open(f'{shelfSavePath}')
                user_file[user_to_find].print_user()
                add_accounts(user_file[user_to_find])
                    
            else:
                print('ERROR: User does not Exist')
                print('Please Create a New User')
                print('')

        
        elif use_command == 'done':
            run = False
        
        else:
            print('Invalid Command. Please Try Again.')
            print('(find, new, done)')
            print('')
main()




