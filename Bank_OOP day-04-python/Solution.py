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
        if amount <= self.balance + self.overdraftLimit:
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
    



class LoanAccount:
    def __init__(self, accountNumber, accountHolder, loanAmount, interestRate) -> None:
        # super().__init__(accountNumber, accountHolder, balance)
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.loanAmount = loanAmount
        self.interestRate = interestRate

    def repay(self, amount):
        if amount > 0 and amount <= self.loanAmount:
            self.loanAmount -= amount
        # print(self.loanAmount)


    def calculateInterest(self):
        interest = self.loanAmount * self.interestRate
        # self.loanAmount = interest
        # print(interest, self.loanAmount)
        return interest
    
    def getOutstandingLoan(self):
        return self.loanAmount
    




class Person:
    def __init__(self, personID, name) -> None:
        self.personID = personID
        self.name = name
        self.accounts = []
        self.relationships = []

        
    def addAccount(self, account):
        self.accounts.append(account)
    
    def addRelationship(self, person):
        if person not in self.relationships:
            self.relationships.append(person)

    def getAccounts(self):
        return self.accounts
    

class Transaction:
    def __init__(self, id, accountNumber, type, amount, time) -> None:
        self.id = id
        self.accountNumber = accountNumber
        self.type = type
        self.amount = amount
        self.time = time

    def __str__(self) -> str:
        return f"{self.id}, {self.accountNumber}, {self.type}, {self.amount}, {self.time}"