# Enums
FIVES = 0
TENS = 1
TWENTIES = 2
INCREMENT = "+"
DECREMENT = "-"


class Solution:
    def __init__(self):
        self.curr_bill_index = -1
        self.cash_register = []
        self.last_bill_index = 0

    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        self.last_bill_index = len(bills) - 1
        self.cash_register = self.init_cash_register()
        return self.check_change_for_customers(bills)

    def init_cash_register(self):
        return [0, 0, 0]

    def take_next_bill(self, bills):
        self.curr_bill_index += 1
        bill = bills[self.curr_bill_index]
        return bill

    def check_change_for_customers(self, bills):
        while self.curr_bill_index != self.last_bill_index:  # Iterate through bills from customers
            bill = self.take_next_bill(bills)

            if bill == 5:
                self.cash_register[FIVES] += 1
                print("fives:", self.cash_register[FIVES])
            elif bill == 10 or bill == 20:
                if not self.have_change(bill):
                    return False
        return True

    def have_change(self, bill):
        if bill == 10:
            if self.cash_register[FIVES] > 0:
                self.cash_register[FIVES] -= 1
                self.cash_register[TENS] += 1
                print("fives:", self.cash_register[FIVES])
                print("tens:", self.cash_register[TENS])
                return True

        elif bill == 20:
            if self.cash_register[TENS] > 0 and self.cash_register[FIVES] > 0:  # Todo: how to know which key to get
                self.cash_register[TENS] -= 1
                self.cash_register[FIVES] -= 1
                print("fives:", self.cash_register[FIVES])
                print("tens:", self.cash_register[TENS])
                return True

            if self.cash_register[FIVES] > 2:
                self.cash_register[FIVES] -= 3
                print("fives:", self.cash_register[FIVES])
                print("tens:", self.cash_register[TENS])
                return True

        return False

s = Solution()
print(s.lemonadeChange([5,5,5,5,10,5,10,10,10,20]))