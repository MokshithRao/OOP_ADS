class DigitalWallet:
	def __init__(self):
		self.balance = 0.0
		self.transaction_history = []

	def initialize_wallet(self):
		# self.balance = 0.0
		# self.transaction_history = []
		print("Wallet initialized with balance 0 and empty transaction history.")

	def display_balance(self):
		# print(self.balance)
		print(f"Current balance: {self.balance:.1f}")

	def add_funds(self, amount):
		# print(type(amount),amount)
		if int(amount) > 0:
			self.balance += int(amount)
			self.transaction_history.append(f"+{float(amount)}")
			print(f"Balance updated to {self.balance}, transaction history logged.")
		else:
			print("Invalid amount. Transaction not recorded.")

	def make_payment(self, amount):
		if int(amount) > 0 and int(amount) <= self.balance:
			self.balance -= int(amount)
			# print("1",self.balance)
			self.transaction_history.append(f"-{float(amount)}")
			print(f"Balance updated to {self.balance}, transaction history logged.")
		else:
			print("Insufficient balance. Transaction not recorded.")

	def view_transaction_history(self):
		print(f"[{', '.join(self.transaction_history)}]")

	def run_wallet_interface(self):
		while True:
			try:
				s = input().split()
				# print(s)
				if s[0] == 'Method:':
					Method = s[1]
				elif s[0] == 'Inputs:':
					if 'amount=' in s[1]:
						amount = s[1].split('=')[1]
					else:
						amount = None
					if Method == 'display_balance':
						self.display_balance()
					if Method == 'initialize_wallet':
						self.initialize_wallet()
					elif Method == 'add_funds':
						self.add_funds(amount)
					elif Method == 'make_payment':
						self.make_payment(amount)
					elif Method == 'view_transaction_history':
						self.view_transaction_history()
			except:
				break

if __name__ == '__main__':
	w = DigitalWallet()
	w.run_wallet_interface()