"""menu module
"""
from .card import BankCard

class Menu:
    """text display api for the session's menus
    """

    def main_ui(self):
        """print main menu
        """
        print('1. Create an account\n2. Log into account\n0. Exit')
        return input()


    def user_ui(self):
        """print user menu (required being logged in)
        """
        print('1. Balance\n2. Log out\n0. Exit')
        return input()


    def __display_created_account(self, u_id: str, u_pin: str):
        """print created account info (id and pin)

        :param u_id str: [newly created id] :param u_pin str: [newly created pin]
        """
        print(f'Your card has been created\nYour card number:\n{u_id}\nYour card PIN:\n{u_pin}')


    def main_create(self, acc_list: dict):
        """create a new account for the user

        :param acc_list dict: [list of accounts created for this interactive session]
        """
        u = BankCard()      # create a new BankCard (i.e. new account)
        self.__display_created_account(u.id, u.pin)
        # save card to session's list of created accounts:
        if not acc_list:
            acc_list = {u.id: u}
        else:
            acc_list[u.id] = u
        return u, acc_list
    

    def main_attempt_login(self, acc_list: dict):
        """print an interactive state for each login attempt

        :param acc_list dict: [collection of accounts created for this session]
        :param u_acc BankCard: [the user account to check against the collection]
        """
        print('Enter your card number:')
        u_num = input()
        print('Enter your PIN:')
        u_pin = input()
        print()

        if u_num not in acc_list or u_pin != (acc_list[u_num]).pin:
            print('Wrong card number or PIN!\n')
            return False, None
        else:
            print('You have successfully logged in!\n')
            return True, acc_list[u_num]


    def user_exit(self):
        """exit the session
        """
        print('Bye')
        exit()


