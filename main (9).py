class Bankaccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("deposited ${}. new balance:${}".format(amount,self.__account_balance))
    else:
       print("invalid deposit amount!please deposit a positive amount.")
  def withdraw(self,amount):
     if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount 
      print("withdraw ${}. new balance: ${}".format(amount,self.__account_balance))
     else:
      print("inavlid withdraw! amount or insufficient balance.")
  def  display_balance(self):
     print("account balance for {} (account #{}): ${}" .format(self.__account_holder_name, self.__account_number,self.__account_balance))
account = Bankaccount(account_number="123456789",account_holder_name="sharumathi",initial_balance=5000.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()