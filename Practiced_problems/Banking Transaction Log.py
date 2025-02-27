class Transaction:
    def __init__(self, transactionID, accountNumber, amount, transactionType):
        self.transactionID = transactionID
        self.accountNumber = accountNumber
        self.amount = amount
        self.transactionType = transactionType
    
    def getTransactionDetails(self):
        return f"{self.transactionID}, {self.accountNumber}, {self.amount}, {self.transactionType}"
    

class BankAccount:
    def __init__(self, accountNumber, balance) -> None:
        self.accountNumber = accountNumber
        self.balance = balance
        self.transactions = []

    def performTransaction(self, transaction):
        if transaction.transactionType == "deposit":
            self.balance += transaction.amount
            self.transactions.append(transaction)
            return True
        elif transaction.transactionType == "withdrawal":
            if self.balance >= transaction.amount:
                self.balance -= transaction.amount
                self.transactions.append(transaction)
                return True
            else:
                return False
        else:
            return False
        
    def getBalance(self):
        return self.balance
    
    def listTransactions(self):
        return self.transactions






def main():
    # Create a bank account
    account = BankAccount("ACC001", 1000.0, "checking")

    # Create transactions
    deposit = Transaction(1, "ACC001", 250.0, "deposit")
    withdrawal = Transaction(2, "ACC001", 100.0, "withdrawal")
    invalid_withdrawal = Transaction(3, "ACC001", 2000.0, "withdrawal")

    # Process deposit
    processed_deposit = account.performTransaction(deposit)
    print("Deposit processed:", processed_deposit)
    print("Balance after deposit:", account.getBalance())

    # Process valid withdrawal
    processed_withdrawal = account.performTransaction(withdrawal)
    print("Withdrawal processed:", processed_withdrawal)
    print("Balance after withdrawal:", account.getBalance())

    # Process invalid withdrawal (should fail)
    processed_invalid = account.performTransaction(invalid_withdrawal)
    print("Invalid withdrawal processed (should be False):", processed_invalid)

    # List transactions
    print("Transaction log:")
    for t in account.listTransactions():
        print(t.getTransactionDetails())


if __name__ == '__main__':
    main()


