class InsufficientFundsError(Exception):
    pass
class BankAccount:
 def __init__ (self,owner,balance):
    self.owner=owner
    self.balance=balance
    
 def deposit(self,amount):
    self.balance=self.balance+amount    

 def withdraw(self,amount):
    if amount>self.balance:
        raise InsufficientFundsError("Dont have sufficient balance")
    self.balance=self.balance-amount

 def get_balance(self):
    return self.balance

 def transaction_history(self):
    return self.history

 def __str__(self):
    return f"Account owner:{self.owner} Balance:{self.balance}"

class SavingsAccount(BankAccount):
 def __init__(self, owner, balance,interest_rate):
    super().__init__(owner, balance)
    self.interest_rate=interest_rate

 def apply_interest(self):
    self.balance*self.interest_rate/100

class CurrentAccount(BankAccount):
   def __init__(self, owner, balance,overdraft_limit):
      super().__init__(owner, balance)
      self.overdraft_limit=overdraft_limit
   def withdraw(self,amount):
      


