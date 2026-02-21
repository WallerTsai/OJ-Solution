from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.total_number = len(balance)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        return self.withdraw(account1, money) and self.deposit(account2, money)
            

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
    
    def is_valid(self, account: int) -> bool:
        return 1 <= account <= self.total_number    # 错误 transfer 可能存在前者有效，先扣钱，而后者无效，钱没回去
    

class Bank:

    def __init__(self, balance: List[int]):
        self.total_number = len(balance)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid(account1) or not self.is_valid(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True
            

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
    
    def is_valid(self, account: int) -> bool:
        return 1 <= account <= self.total_number