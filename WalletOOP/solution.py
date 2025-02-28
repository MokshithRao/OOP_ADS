from sol import ArrayListADT

class Transaction:
    def __init__(self, type, amount, fee) -> None:
        self.type = type
        self.amount = amount
        self.fee = fee
    
    def __str__(self):
        return f"{self.type} {self.amount} (Fee: {self.fee})"




class Wallet:
    def __init__(self, withdrawalLimit, withdrawalFeePercentage):
        self.balance = 0.0
        self.transactions = ArrayListADT()
        self.withdrawalLimit = withdrawalLimit
        self.withdrawalFeePercentage = withdrawalFeePercentage


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction("DEPOSIT", amount, 0.0)
            self.transactions.add(transaction)
            return f"Deposit of {amount} successful. Current balance: {self.balance}"
        return f"Deposit of {amount} failed. Balance remains: {self.balance}"




    def withdraw(self, amount):
        if amount < 0 and amount > self.balance or amount > self.withdrawalLimit:
            return f"Withdrawal of {amount} failed. Balance remains: {self.balance}"
        else:
            fee = (self.withdrawalFeePercentage/100) * amount
            self.balance -= (amount + fee)
            transaction = Transaction("WITHDRAW", amount, fee)
            self.transactions.add(transaction)
            return f"Withdrawal of {amount} successful with a fee of {fee}. Current balance: {self.balance}"



    def getBalance(self):
        return f"Current Balance: {self.balance}"

    def getTransactions(self):
        history = "Transaction History:\n"
        for i in range(self.transactions.size_()):
            history += f"{i+1}. {self.transactions.get(i)}\n"
        return history.strip()



wallet = None
while True:
    try:
        s = input().split()
        if not s:
            break

        if s[0].isdigit():
            wallet = Wallet(float(s[0]), float(s[1]))
            print(f"Wallet initialized with withdrawalLimit: {wallet.withdrawalLimit}, withdrawalFeePercentage: {wallet.withdrawalFeePercentage}%")

        elif s[0] == 'deposit' and wallet:
            print(wallet.deposit(float(s[1])))

        elif s[0] == 'withdraw' and wallet:
            print(wallet.withdraw(float(s[1])))
        
        elif s[0] == 'getBalance' and wallet:
            print(wallet.getBalance())

        elif s[0] == 'getTransactions' and wallet:
            print(wallet.getTransactions())
        
        else:
            print("Invalid command or wallet not initialized.")
    except:
        break

