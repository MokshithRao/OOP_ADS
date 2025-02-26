class Account:
    def __init__(self, accountNumber, accountHolder, balance) -> None:
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return True
        return False
    

    def getBalance(self):
        return self.balance
    


class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolder, balance, intrestRate) -> None:
        super().__init__(accountNumber, accountHolder, balance)
        self.intrestRate = intrestRate

    def calculateInterest(self):
        intrest = self.balance * self.intrestRate
        self.balance -= intrest
        return intrest



class CurrentAccount(Account):
    def __init__(self, accountNumber, accountHolder, balance, overdraftLimit) -> None:
        super().__init__(accountNumber, accountHolder, balance)
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount):
        if amount < self.balance + self.overdraftLimit:
            self.balance -= amount
            return True
        return False
        # return super().withdraw(amount)