class Account:
    def __init__(self,username,password,amount):
        self.username = username
        self.password = password
        self.amount = amount
    def __rper__(self):
        return f"Account({self.username},{self.amount})"
class BankSystem:
    def __init__(self):
        self.accounts = []
    def create_account(self,username,password,amount):
        for i in self.accounts:
            if i.username == username:
                return "username Already Exists"
            
        new = Account(username,password,amount)
        self.accounts.append(new)
        return "Account created successfully"
    def get_account(self,username,password):
        for i in self.accounts:
            if i.username == username and i.password == password:
                return i
            return False
    def withdraw(self,username,password,amount):
        account = self.get_account(username,password)
        if account == False:
            return "invalid username/password"
        if amount > account.amount:
            return "insufficient balance"
        if amount > 0:
            account.amount -= amount
            return "withdrawn successfully"
        else:
            return "invalid amount"
    def deposit(self,username,password,amount):
        account = self.get_account(username,password)
        if account == False:
            return "invalid username/password"
        if amount > 0:
            account.amount = amount
            return "deposit successfully"
        else:
            return "invalid amount"
BANK = BankSystem()
output = BANK.create_account(username = "coder",password = '123',amount=2000)
print(output)
output = BANK.deposit(username = 'coder',password = '123',amount=1000)
print(output)
output = BANK.withdraw(username = 'coder',password = '123',amount=1000)
print(output)
        
        
