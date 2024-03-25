#Class
#Bank Account

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.account_id = int(account_id)
        self.account_type = str(account_type)
        self.pin = int(pin)
        self.balance = float(balance)

    def deposit(self, money):
        self.money = int(money)
        self.balance = self.balance + money
        print ("You put a deposit of", self.money,"€")

    def withdraw(self, substract):
        self.substract = int(substract)
        self.balance = self.balance - substract
        print ("You took", self.substract,"€ from your account")

    def display_balance(self):
        print ("Your current Balance is:", self.balance)


max = BankAccount ("Maxime", "Denis", 4679, "Depo/WithDraw", 1234, 54)

max.deposit(96)
max.display_balance ()

max.withdraw(17)
max.display_balance ()