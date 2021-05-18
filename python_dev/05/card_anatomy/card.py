# Write your code here
import random
random.seed()

class BankAccount:
    IIN = '400000'
    checksum = str(random.randint(0, 9))
    def __init__(self):
        self.user_id = ''
        self.user_id += self.IIN
        self.user_pin = ''
        self.balance = 0
        for i in range(9):
            x = str(random.randint(0, 9))
            self.user_id += x
        
        self.user_id += self.checksum
        for i in range(4):
            p = str(random.randint(0, 9))
            self.user_pin += p
                

def print_menu():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    return input()

def print_user_menu():
    print('1. Balance')
    print('2. Log out')
    print('0. Exit')
    return input()

accounts = dict()
while True:
    inp = print_menu()
    print()
    if inp == '1':
        # create account
        u = BankAccount()
        print(f'Your card has been created')
        print('Your card number:')
        print(u.user_id)
        print('Your card PIN:')
        print(u.user_pin)
        print()
        if not accounts:
            accounts = { u.user_id: u }
        else:
            accounts[u.user_id] = u
        
    elif inp == '2':
        # log in
        print(accounts)
        print('Enter your card number:')
        u_num = input()
        print('Enter your PIN:')
        u_pin = input()
        print()
        if u_num not in accounts:
            print('Wrong card number or PIN!')
            print()
            continue

        elif u_pin != (accounts[u_num]).user_pin:
            print('Wrong card number or PIN!')
            print()
            continue

        else:
            print('You have successfully logged in!')
            print()
            while True:
                inp = print_user_menu()
                print()
                if inp == '1':
                    print(f'Balance: {accounts[u_num].balance}')
                    print()
            
                elif inp == '2':
                    print('You have successfully logged out!')
                    print()
                    break
            
                elif inp == '0':
                    print('Bye')
                    exit()
        
    elif inp == '0':
        break # exit the program
        
print('Bye')
