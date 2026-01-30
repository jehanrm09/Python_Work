class Bank:
    
    def __init__(you,balance):
        you.balance = balance
    def withdraw(you,amount):
        if amount < 0:
            raise Exception('amount cannot be -ve')
        if you.balance < amount:
            raise Exception('paise nai hai tere paas')
            you.balance = you.balance - amount
obj = Bank(10000)
try:
    obj.withdraw(15000)
except Exception as e:
    print(e)
else:
    print(obj.balance)
