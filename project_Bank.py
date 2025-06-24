from datetime import datetime

class AccountBank:
    
    def __init__(self,name: str,iban: str ,balance:float):
        self.name=name
        self._iban=iban
        self.balance=balance
        
    def get_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        
    def withdrawal(self,amount:float):
        if amount<=self.balance:
            self.balance = self.balance - amount  
            print(f'the amount withdrawal= {amount} , in time [{self.get_time()}] ')
            
        elif amount>self.balance:
            print('Insufficient funds')
            
    def Deposit(self,amount):
        #handle deposit with 0 or less
        if amount<=0:
            print('The amount should be more than zero')
        elif amount>0:
            self.balance=self.balance + amount
            #add the balance in the print message
            print(f'the amount Deposit {amount} , in time [{self.get_time()}] ')
            
    
    def accountinfo (self):
         print(f' [{self.get_time()}] Name:  {self.name}')
         print(f'[{self.get_time()}] Iban: {self._iban}')
         print(f'[{self.get_time()}] Balance: {self.balance}' )
         
class investment_Account(AccountBank): 
    
    def __init__(self, name, iban, balance):
        super().__init__(name, iban, balance)
        self.deposits = []  # ✅ الاسم الصحيح والمناسب
        
    
    def Deposit(self,amount):
        #handle deposit with 0 or less
        if amount<=0:
            print('The amount should be more than zero')
        elif amount>0:
            self.balance=self.balance + amount
            deposit_time=datetime.now() 
            self.deposits.append((amount, deposit_time))
            print(f'Deposited {amount} at [{self.get_time()}]')
            
    def withdrawal(self, amount):
        total_available = 0
        now = datetime.now()

        for deposit_amount, deposit_time in self.deposits:
            if (now - deposit_time).days >= 365:
                total_available += deposit_amount

        if amount <= total_available:
            self.balance -= amount
            print(f'Withdrawal = {amount}, in time [{self.get_time()}]')
        else:
            print("You can only withdraw funds that have been deposited for at least 1 year.")
 
    #getter   
    @property
    def iban(self):
        return self.__iban
    
    #setter
    @iban.setter  
    def iban(self,new_iban):
        if  (
        isinstance(new_iban, str) and
        len(new_iban) == 10 and
        new_iban[:2].isalpha() and
        new_iban[2:].isdigit()
        ):
            print(f'Iban updated successfully to: {new_iban}')
        else:
            print('Invalid IBAN. It must be a string with at least 10 characters.')
    
    
    def accountinfo (self):
         print(f' [{self.get_time()}] Name:  {self.name}')
         print(f'[{self.get_time()}] Iban: {self._iban}')
         print(f'[{self.get_time()}] Balance: {self.balance}' )
    
# BandarAccount= AccountBank("Bandar Al-Rasheed", "SA34567890", 500)
# BandarAccount.withdrawal(100)
# BandarAccount.Deposit(200)
# BandarAccount.iban='SA34567891'
# print(BandarAccount.iban) 
# BandarAccount.accountinfo() 
b=investment_Account('najem','SA60801578',3000 )
b.withdrawal(100)

b.accountinfo()
# ///////////////////////////////////////////////////////////////////////////// 

#class device  def __init__(self,name: str,cost: str ,storage:float):


#class mobile inherit device
# def __init__(camera, applications):


#class laptop inherit device
# def __init__(camera, keyboard):



