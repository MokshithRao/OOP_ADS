class Account:
    def __init__(self, accountNumber, account_holder, balance) -> None:
        self.accountNumber = accountNumber
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    

    def getBalance(self):
        return self.balance
    


class SavingsAccount(Account):
    def __init__(self, accountNumber, account_holder, balance, intrest_rate) -> None:
        super().__init__(accountNumber, account_holder, balance)
        self.intrest_rate = intrest_rate

    def calculateInterest(self):
        intrest = self.balance * self.intrest_rate
        self.balance -= intrest
        return intrest



class CurrentAccount(Account):
    def __init__(self, accountNumber, account_holder, balance, overdraft_limit) -> None:
        super().__init__(accountNumber, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False





class Bank:
    def __init__(self) -> None:
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def findAccount(self, accountNumber):
        for account in self.accounts:
            if account.accountNumber == accountNumber:
                return account
        return None
        
    def transfer(self, From_account_number, To_account_number, amount):
        From_acc = self.findAccount(From_account_number)
        To_acc = self.findAccount(To_account_number)
        
        if From_acc.withdraw(amount):
            To_acc.deposit(amount)
            return True
        
        return False
    



class LoanAccount:
    def __init__(self, accountNumber, account_holder, loan_amount, interest_rate) -> None:
        # super().__init__(accountNumber, accountHolder, balance)
        self.accountNumber = accountNumber
        self.account_holder = account_holder
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate

    def repay(self, amount):
        if amount > 0 and amount <= self.loan_amount:
            self.loan_amount -= amount
        # print(self.loanAmount)


    def calculateInterest(self):
        return self.loan_amount * self.interest_rate
    
    def getOutstandingLoan(self):
        return self.loan_amount
    



class Person:
    def __init__(self, person_id, name) -> None:
        self.person_id = person_id
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