class bank:
    def __init__(self,accn,num,accty,):
        self.accn=accn
        self.num=num
        self.accty=accty
        self.bal=0

    def showamt(self):
        print("Account Holder Name ",self.accn)
        print("Account number",self.num)
        print("Account type",self.accty)
        print("Account balance",self.bal)
    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withd(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("Enter your name : ")
a=int(input("Enter your Account Number : "))
t=input("Enter you Account Type : ")
o=bank(n,a,t)
o.showamt()
while(True):
    print("\nMenu")
    print("\n1.Deposit")
    print("\n2.Withdraw")
    c=int(input("\nEnter your choice"))
    # d=0
    if(c==1):
        d=int(input("Enter the amount to be deposit : "))
        print("Your Total Balance Amount is ", o.dep(d))
    elif(c==2):
        w=int(input("Enter the Amount to be withdraw : "))
        if(w>d):
            print("Insufficent Balance")
        else:
            print("Your Total balance Amount is : ",o.withd(w))
    else:
        print("Invalid choice")