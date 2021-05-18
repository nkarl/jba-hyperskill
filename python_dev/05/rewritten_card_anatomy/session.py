"""main module
"""
import card

class Menu:
    def main_ui(self):
        """
        print main menu

        """
        print('1. Create an account\n2. Log into account\n0. Exit')
        return input()

    def user_ui(self):
        """
        print user menu (required being logged in)

        """
        print('1. Balance\n2. Log out\n0. Exit')
        return input()

    def user_create(self, u_id: str, u_pin: str):
        """
        print created account info (id and pin)

        :param u_id str: [newly created id]
        :param u_pin str: [newly created pin]
        """
        print(f'Your card has been created\nYour card number:\n{u_id}\nYour card PIN:\n{u_pin}')

    def option_create(self, acc_list: dict):
        """
        create a new account for the user

        :param acc_list dict: [list of accounts created for this interactive session]
        """
        u = card.BankCard()
        self.user_create(u.id, u.pin)
        # save card to session's list of created accounts:
        if not acc_list:
            acc_list = {u.id: u}
        else:
            acc_list[u.id] = u
        return u, acc_list
    
    def user_attempt_login(self, acc_list: dict, u_acc: card.BankCard):
        """
        print an interactive state for each login attempt

        :param acc_list dict: [collection of accounts created for this session]
        :param u_acc card.BankCard: [the user account to check against the collection]
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
        """
        exit the session

        """
        print('Bye')
        exit()


# start a new session:
session = True
while session is True:
    accounts = dict()
    interaction = Menu()

    IN_MAIN_MENU = True
    while IN_MAIN_MENU:
        u_input = interaction.main_ui()
        if u_input == '1':
            u, accounts = interaction.option_create(accounts)

        elif u_input == '2':
            is_logged, u = False, None

            while not is_logged:
                is_logged, u = interaction.user_attempt_login(accounts, interaction)
            else:
                IN_USER_MENU = True
                while IN_USER_MENU:
                    u_input = interaction.user_ui()
                    if u_input == '1':
                        print(f'Balance: {u.balance}\n')
                    elif u_input == '2':
                        print('You have successfully logged out!\n')
                        IN_USER_MENU = False
                    elif u_input == '0':
                        interaction.user_exit()

        elif u_input == '0':
            interaction.user_exit()

