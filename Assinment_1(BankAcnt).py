class BankAccount:
    def __init__(self,Number,Name,Balance = 500.0):
        self.name = Name
        self.number = Number
        self.balance = Balance
    def deposit(self,amount):
        self.balance += amount
        print("Amount of ", amount,"Deposited Succesfully to", self.name)
        print("Balance : Rs", self.balance)        
    def withdraw(self,amount):
        if self.balance<amount:
            print("Not Enough Balance")
        else:
            self.balance -= amount
            print("Amount withdrawn from account",self.name," :Rs", amount)
            print("Balance : Rs",self.balance)
    def getBalance(self,number,name):
        if number == self.number and name == self.name:
            print("Current Total Balance: Rs",self.balance)
        else:
            print("Please enter currect Account name or number")
    def __str__(self):
        return f"Account-> {self.number} \n Name->{self.name} \n balance-> {self.balance}"
    
class SavingsAccount(BankAccount):
    def __init__(self, Number, Name,interest_rate, Balance=0):
        super().__init__(Number, Name, Balance) 
        self.interest_rate = interest_rate
    def applyintrest(self):
        intrest = self.balance * self.interest_rate / 100
        print("Intrest @",self.interest_rate,"%: Rs" , intrest)
        self.balance += intrest
        print("Balance after Intrest : Rs", self.balance)
class CurrentAccount(BankAccount):
    def __init__(self, Number, Name, overdraft_limit,Balance=0):
        super().__init__(Number, Name, Balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Limit Excedded please give less input")
        else:
            self.balance -= amount
            print("Money withdrawn from account ",self.name," : Rs",amount)
            print("Current Balance : Rs",self.balance)
class Fixeddeposit(BankAccount):
    def __init__(self, Number, Name,lock_period ,Balance=0):
        super().__init__(Number, Name, Balance)
        self.lock_period = lock_period
        self.month = 0

    def withdraw(self, amount):
        if self.month < self.lock_period:
            print("Time period is not over can't withdraw")
        else:
            super().withdraw(amount)
    def pass_month(self):
        self.month += 1

savingA = SavingsAccount("SA_11" ,"Siddarth",10,80000)
currentA = CurrentAccount("CA_22","Kedarnath",20000,60000)
FixedAcnt = Fixeddeposit("FA_33","Ramlingam",6,4000.00)
print("Performing deposit : ")
savingA.deposit(5000)        
currentA.deposit(10000)        
print()
print("Performing withdrawal")
savingA.withdraw(5000)
currentA.withdraw(30000)
print()
print("Demonstrate Intrest on savings")
savingA.applyintrest()
print()
print("Overdraft limit")
currentA.withdraw(50000)

class bank:
    def __init__(self):
        self.accounts = {}
    def addaccount(self,account):
        if account.number in self.accounts:
            print("Account Already Exists")
        else:
            self.accounts[account.number] = account
    def getaccount(self,number):
        if number in self.accounts:
            return self.accounts.get(number)
    def transfer(self,from_number,to_number,amount):
        from_act = self.getaccount(from_number)
        to_act = self.getaccount(to_number)
        if not from_act or not to_act :
            print("One or Both accounts not Exists")
        else:
            print(f"Successfully transfered Rs {amount} from {from_act.name} to {to_act.name}")
            from_act.withdraw(amount)
            to_act.deposit(amount)
            
Bosch_Bank = bank()

Bosch_Bank.addaccount(savingA)
Bosch_Bank.addaccount(currentA)
Bosch_Bank.addaccount(FixedAcnt)
print()
FixedAcnt.pass_month()
FixedAcnt.pass_month()
FixedAcnt.pass_month()

print(Bosch_Bank.getaccount("CA_22"))

print()
Bosch_Bank.transfer("SA_11","CA_22",5000)