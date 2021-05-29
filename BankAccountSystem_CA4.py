#Student name : Daniel Fox
#COMP517 Assignment 4 - Bank Account
import random
import datetime
"""The program acts as a bank account, with two types of account. The first account is Basic this doesnt allow any overdraft options.
The second account is a Premium account which allows overdraft options and the programmer can set and change the overdraft. The account cannot be closed if their is an negative balance from overdraft"""
class BasicAccount:
    """Basic Account: name:string, acNum=int, balance=float, cardNum=string, cardExp=tuple(int,int).  
       The account can deposit, withdraw, checkAailableBalance, getBalance,printBalance,getName,getAcNum,
       issueNewCard,closeAccount.
    """
    #Had to use a global to increment the account number, then place this value into self.AcNum
    GlobalAcNum=0
    def __init__(self,name,OpeningBalance):
        """Inits Basic Account giving the account name, opening balance from user
            acNumber set at 1 for the first account created and then increments 
            with multiple instances.
            There is no overdraft available for basic account
        """
        self.acName=name#string
        self.acNum=1#int
        
        self.balance=OpeningBalance #float
        self.cardNum="Not Set"#string
        self.cardExp=0,0#tuple

        self.AccountClosure=False ##initialize and set to false
        
        #Assumption basic account cannot overdraft, if the user has an opening balance of negative, the program wont allow the user to close their account until the negative balance is equal 0 
        self.overdraft=False #initialize to remove duplicate function in child  
        self.overdraftLimit=0#initialize to remove duplicate function in child  
    
        #Tests if user has input a number if not sets blance to zero
        if isinstance(self.balance,float) or isinstance(self.balance,int)==True:
            self.balance=float(self.balance)
        else:
            print("%ss Account,WARNING! Opening balance not a number, Opening balance value set to zero." %self.acName)
            self.balance=0.00

        
        
    def __str__(self):
        """Info prinintg the Basic account informaation: account name , account number , balance, card number and expiry date """
        return 'Hello,{self.acName} your account number is:{self.acNum}, your current bank balance is: {self.balance}. Your card number is {self.cardNum} and expiry date is {self.cardExp}.'.format(self=self)

    
    def getName(self):
        """Returns the name of the account holder as a string"""
        print("Hello %s,Account type: Basic" %self.acName)

    def deposit(self): 
        """Deposits the stated amount into the account, and adjusts the balance appropriately.
        Deposits must be a positive amount."""
        while True:
            try:
                amount=float(input("Enter the amount you wish to deposit(£):\n£"))
                if amount<0:
                    print("Invalid amount, You cant input a negative amount")
                    continue
                break
            except ValueError:
                print("You value is not an int")
        self.balance+=amount
        overdraftAmount=self.overdraftLimit #Wont allow the use of self.overdraft unless overdraftAmount is initalized
        if self.balance>=0:
            print("Deposited £%.2f.Your total balance is now £%.2f"%(amount,self.balance))
            return self.balance
        else:
            #Creating a variable to store overdraft limit for negative balance calulcation and updating overdraftlimit
            print("In Overdraft (Negative balance)")
            self.overdraftlimit=overdraftAmount+self.balance #updates overdraft limit
            return self.balance
      
    
    def withdraw(self):
        amount=float(input("Enter the amount you wish to withdraw:\n£"))
        if self.overdraft==False:
            if amount>self.balance:
                print("Insufficient funds. Can not withdraw")
            else:
                self.balance -= amount
                print("Withdrawn £%.2f.Your new balance:£%.2f"%(amount,self.balance))
                return self.balance
        #Only run this for premium account
        if self.overdraft==True:
            overdraftAmount=self.overdraftLimit
            #checking if balance is less than the overdraft limit
            if self.balance<-overdraftAmount:
                print("Cannot withdraw balance of:",self.balance)
            if amount>(self.balance+overdraftAmount):
                print("DENIED!! Withdrawl over limit")
            else:
                print("Withdrawing balance...")
                self.balance-=amount#minus amount
                #checks if balance is less than zero if it is , there is an overdraft calculation
                if self.balance<0:
                    self.overdraftLimit=overdraftAmount+self.balance#plus because self.balance would be negative
                    #print("Balance negative")
            
    def getAvailableBalance(self):
        """Returns the total balance that is available in the account as a float. Account type basic has no overdraft option to return"""
        return float(self.balance)
    def getBalance(self):
        """Returns the total balance that is available if account is overdrawn show negative balance"""
        return float(self.balance)
    def printBalance(self):
        "Print balance of account and state what overdraft is remaining"
        print("Current Balance is:£%.2f.Basic account has no overdraft option"%self.balance)

#Set the self.AcNum equal to the global AcNum
    def getAcNum(self):
        BasicAccount.GlobalAcNum+=1
        self.acNum=BasicAccount.GlobalAcNum
        print("The Account number is:",self.acNum)
        return self.acNum

    # def issueNewCard(self):
    #     """Creates a new card number, with the expiry being 3 years to the month from now. (eg: if today is 3/12/20, then the expiry date would be (12/23))"""
    #     #Wasnt clear on what to do, I just made card number random
    #     list1=[]
    #     numGen="123456789"
    #     str1=""
    #     self.expiry=[]
    #     while True:
    #         for i in range(16):
    #             str1+=random.choice(numGen)
    #         if str1 not in list1:
    #             list1.append(str1)
    #             break
    #     self.cardNum=str(list1)
    #     self.cardNum=' '.join([self.cardNum[i:i+4] for i in range(0, len(self.cardNum), 4)])
    #     print("Your card number is:",self.cardNum)
        
    #     #Expiry date every 3 years
    #     today = datetime.datetime.now()

    #     ExpMonth=today.month
    #     ExpYear=str(today.year+3)
    #     ExpYear=int(ExpYear[2:])
        
    
    #     self.cardExp=ExpMonth,ExpYear
        
    #     print("Card Expiry date =", self.cardExp)
    #     return self.cardNum, self.cardExp

    def closeAccount(self):
        beforeClose=self.balance
        if(beforeClose<0):
            print("Your balance is negative: £%.2f, You cannot close your account as you're in an overdraft." %(self.balance))
            self.AccountClosure=False
            print("Is account closed?",self.AccountClosure)
        else:
            self.balance-=beforeClose
            print("Withdrawing all money to customer..")
            print("Success! £%.2f has been withdrawn, the remaining balance is now £%.2f"%(beforeClose,self.balance))
            #Making sure all money has been withdrawn before closure of account
            if self.balance==0:
                self.AccountClosure=True 
                print("Is account closed?",self.AccountClosure)
            else:
                self.AccountClosure=False
                print("Error.. not all money has been transfered out of the account, unable to close")
                print("Is account closed?",self.AccountClosure)
        
        return self.AccountClosure


#Child account
class PremiumAccount(BasicAccount):
    """Premium Account: inhertis variables from Basic Account parent class.  
       The premium account allows an overdraft and this can be set. 
       The account can deposit, withdraw, checkAailableBalance, getBalance,printBalance,getName,getAcNum,
       issueNewCard,closeAccount,setOverdraftLimit.

       Assumption Overdraft is set True even if the account doesnt require an overdraft, The Programmer can set the overdraft limit to 0 if they wish.
    """
    def __init__(self,name,openingBalance,initialOverdraft):
        """Initialiser giving the account name and opening balance"""
        super().__init__(name,openingBalance)
        self.acName=name
        self.initialOverdraft=initialOverdraft
        self.overdraftLimit=500.00 #pounds  #DOESNT take into account initial overdraft, the initial is calcualted into the opening balance
        self.balance=openingBalance-self.initialOverdraft 
    
        self.overdraft=True
       

    def __str__(self):
        """string representations for the account name, available balance, and overdraft details"""
        return 'Hello,{self.acName} your account number is:{self.acNum}, your current bank balance is:£{self.balance} with an inital overdraft of:£{self.initialOverdraft}.Your Overdraft limit available is:£{self.overdraftLimit}. Your card number is {self.cardNum} and expiry date is {self.cardExp}.'.format(self=self)
 
    def getName(self):
        """Print account name"""
        print("Premium account:\nHello,",self.acName)


    def getAvailableBalance(self):
        """Returns the total balance that is available in the account as a float. It should also take into account any overdraft that is available."""
        return float(self.balance)


    def printBalance(self):
        "Print balance of account and state what overdraft is remaining"
        print("Current Balance available is:£%.2f.The overdraft remaining is £%.2f" %(self.balance,self.overdraftLimit))


    def setOverdraftLimit(self):
        """Sets overdraft limit to certain amount"""
        print("Setting up a new Overdraft limit.\n")
        newLimit=float(input("Enter the overdraft limit amount:\n£"))
        self.overdraftLimit=newLimit
        return self.overdraftLimit

                
def main():
    print("BASIC ACCOUNT")
    print("*************************************")
    Account1=BasicAccount("Dan",100)
    account3=PremiumAccount("Jane Doe", 0, 0)
    # Account1.deposit()
    # Account1.withdraw()
    # Account1.getAvailableBalance()
    # Account1.printBalance()
    #Account1.closeAccount()
    # account3.deposit()
    # account3.printBalance()
    # account3.withdraw()
    # account3.getAvailableBalance()
    # account3.getAvailableBalance()
    # account3.printBalance()
    account3.closeAccount()
    # print('name type',type(Account1.acName))
    # print('acNum type',type(Account1.acNum))
    # print('balance type',type(Account1.balance))
    # print('card num type',type(Account1.cardNum))
    # print('card exp type',type(Account1.cardExp))
    # print(Account1.acName)
    # print(Account1.acNum)
    # print(Account1.balance)
    # print(Account1.cardNum)
    # print(Account1.cardExp)
    # print('init type',type(Account1.__init__))
    # print('str type',type(Account1.__str__))
    # # print('deposit type',type(Account1.deposit()))
    # # print('withdraw type',type(Account1.withdraw()))
    # print('get avail balance type',type(Account1.getAvailableBalance()))
    # print('get balance type',type(Account1.getBalance()))
    # print('print balance type',type(Account1.printBalance()))
    # print('get name type',type(Account1.getName()))
    # print('get acnum  type',type(Account1.getAcNum()))
    # print('issue new card type',type(Account1.issueNewCard()))
    # print('close account type',type(Account1.closeAccount()))
    # print("*************************************")
    # print()
    # print()
    # print("*************************************")
    # print("*************************************")
    # print("PREMIUM ACCOUNT")
    # print("*************************************")
    # print('name type',type(account3.acName))
    # print('acNum type',type(account3.acNum))
    # print('balance type',type(account3.balance))
    # print('card num type',type(account3.cardNum))
    # print('card exp type',type(account3.cardExp))
    # print('overdraft limit type',type(account3.cardExp))
    # print('overdraft type',type(account3.cardExp))
    # print(account3.acName)
    # print(account3.acNum)
    # print(account3.balance)
    # print(account3.cardNum)
    # print(account3.cardExp)
    # print(account3.overdraftLimit)
    # print(account3.overdraft)
    # print('init type',type(account3.__init__))
    # print('str type',type(account3.__str__))
    # # print('deposit type',type(account3.deposit()))
    # # print('withdraw type',type(account3.withdraw()))
    # print('get avail balance type',type(account3.getAvailableBalance()))
    # print('get balance type',type(account3.getBalance()))
    # print('print balance type',type(account3.printBalance()))
    # print('get name type',type(account3.getName()))
    # print('get acnum  type',type(account3.getAcNum()))
    # print('issue new card type',type(account3.issueNewCard()))
    # print('close account type',type(account3.closeAccount()))
    # # print('set overdraftlimit type', type(account3.setOverdraftLimit()))
    # print("*************************************")

if __name__ == "__main__":
    main()

