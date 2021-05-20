"""submodule containing the class bank card
"""
import random

class BankCard:
    """a class for Bank Card.
    """
    random.seed()
    bank_iin = '400000'     # the IIN pertaining to this bank institution
    id_len = 9
    pin_len = 4

    def __init__(self):
        self.id  = self.__generate_card_id()        # client-card's id
        self.pin = self.__generate_pin()            # client-card's pin
        self.balance = 0


    def __generate_checksum(self, sequence: list):
        """generate a checksum for a given sequence

        :param sequence str: the sequence of digits
        """
        aa = sequence
        # second, double all digits whose index is even:
        bb = [v * 2 if i % 2 == 0 else v for i, v in enumerate(aa)]
        # third, subtract 9 from any digits larger than 9
        cc = list(map(lambda x: x - 9 if x > 9 else x, bb))
        # fourth, take the sum of the sequence
        dd = sum(cc)
        # finally, find the checksum that satifies: (dd + checksum) % 10 == 0 
        ee = dd
        while ee % 10 != 0:
            ee += 1
        return (ee - dd)


    def __generate_card_id(self):
        """generate a new unique card id
        """
        # first, generate a sequence of random numbers, length defined as id_len:
        unique_id = [random.randint(0, 9) for i in range(self.id_len)]
        # second, combine into a 15-digit sequence:
        card_id = (list(map(int, self.bank_iin))) + unique_id
        # third, generate a checksum from that sequence:
        checksum = self.__generate_checksum(card_id)

        id = ''.join(map(str, card_id + [checksum]))
        return id


    def __generate_pin(self):
        """generate a new pin
        """
        new_pin = [random.randint(0,9) for i in range(self.pin_len)]
        return ''.join(map(str, new_pin))

