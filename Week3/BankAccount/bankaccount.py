class BankAccount:

    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError("Start balance must be >= 0")
        self.name = name
        self._balance = balance
        self.currency = currency
        self.history_list = []
        self.history_list.append("Account was created")

    def deposit(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.history_list.append("Deposited: {}{}".format(amount, self.currency))
            self._balance += amount
        else:
            raise ValueError("Invalid Amount!")

    def balance(self):
        self.history_list.append("Balance check -> {}{}".format(self._balance, self.currency))
        return self._balance

    def withdraw(self, amount):
        if amount <= self.balance():
            self.history_list.append("{}{} was withdrawed".format(amount, self.currency))
            self._balance -= amount
            return True
        return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self._balance, self.currency)

    def __int__(self):
        self.history_list.append("__int__ check -> {}{}".format(self._balance, self.currency))
        return self._balance

    def transfer_to(self, account, amount):
        if self.currency == account.currency:
            self.history_list.append("Transfer to {} for {}{}".format(account.name, amount, self.currency))
            account.history_list.append("Transfer from {} for {}{}".format(self.name, amount, self.currency))
            account._balance += amount
            self._balance -= amount
            return True
        else:
            raise ValueError("Currencies not the same!")

    def history(self):
        return self.history_list



account = BankAccount("Rado", 0, "$")
account.deposit(1000)
rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")

print(account.balance())
print(str(account))
print(int(account))
print(account.history())
print(account.withdraw(500))
print(account.balance())
print(account.history())
print(account.withdraw(1000))
print(account.balance())
print(account.history())

print(rado.transfer_to(ivo, 500))
print(rado.balance())
print(ivo.balance())
print(rado.history())
print(ivo.history())
