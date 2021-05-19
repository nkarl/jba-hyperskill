"""session module
"""
from backend.menu import Menu

# start a new session:
def session():
    session = True
    while session is True:
        accounts = dict()       # list of accounts created for this session
        interaction = Menu()    # start a new interactive api object

        IN_MAIN_MENU = True
        # while in main menu
        while IN_MAIN_MENU:
            u_input = interaction.main_ui()

            if u_input == '1':
                u, accounts = interaction.main_create(accounts)

            elif u_input == '2':
                is_logged, u = False, None

                # loop back if incorrect id or pin
                while not is_logged:
                    is_logged, u = interaction.main_attempt_login(accounts)

                # otherwise, log in:
                else:
                    IN_USER_MENU = True
                    # while logged in
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


if __name__ == "__main__":
    session()
