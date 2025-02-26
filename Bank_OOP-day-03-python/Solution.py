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



class Bank:
    def __init__(self) -> None:
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def findAccount(self, accountNumber):
        for account in self.accounts:
            if account.accountNumber == accountNumber:
                return account
        
    def transfer(self, fromAccountNumber, toAccountNumber, amount):
        fromAcc = self.findAccount(fromAccountNumber)
        toAcc = self.findAccount(toAccountNumber)
        
        if fromAcc.withdraw(amount):
            toAcc.deposit(amount)
            return True
        
        return False
    
        

