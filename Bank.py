class bank:
    balanca=0
    balancj=0
    balanm=0
    balab=0
    def balance(self):
        amount=int(input('ENTER YOUR AMOUNT:'))
        bank.balanca+=amount
        print("BALANCE=",bank.balanca)
    def balanc(self):
        amount=int(input("ENTER YOUR AMOUNT:"))
        bank.balancj+=amount
        print("BALANCE=",bank.balancj)
    def balan(self):
        amount=int(input('ENTER YOUR AMOUNT:'))
        bank.balanm+=amount
        print('BALANCE=',bank.balanm)
    def bala(self):
        amount=int(input('ENTER YOUR AMOUNT:'))
        bank.balab+=amount
        print('BALANCE=',bank.balab)
    def withdraw(self):
            if bank.balanca>1000:
                amount=int(input('ENTER A AMOUNT:'))
                bank.balanca-=amount
                print("BALANCE=",bank.balanca)
            else:
                print('''SORRY
YOUR BALANCE IS LESS THAN 1000.''')
    def withdra(self):
            if bank.balancj>1000:
                amount=int(input('ENTER A AMOUNT:'))
                bank.balancj-=amount
                print("BALANCE=",bank.balancj)
            else:
                print('''SORRY
YOUR BALANCE IS LESS THAN 1000.''')
    def withdr(self):
            if bank.balanm>1000:
                amount=int(input('ENTER A AMOUNT:'))
                bank.balanm-=amount
                print("BALANCE=",bank.balanm)
            else:
                print('''SORRY
YOUR BALANCE IS LESS THAN 1000.''')
    def withd(self):
            if bank.balab>1000:
                amount=int(input('ENTER A AMOUNT:'))
                bank.balab-=amount
                print("BALANCE=",bank.balab)
            else:
                print('''SORRY
YOUR BALANCE IS LESS THAN 1000.''')    
    def __del__(self):
        print('''THANK YOU
VISIT AGAIN''')
k=bank()
a=1234567890
b=9789043358
c=9940383012
d=9566594962
i=0
while i<=3:
    m='MENU'
    print(m.center(60,'*'))
    print(" 1.DEPOSIT",'\n',"2.WITHDRAW",'\n',"3.EXIT")
    ch=int(input('ENTER YOUR CHOICE(1/2/3):'))
    if ch==1:
        p=int(input("ENTER YOUR ACCOUNT NUMBER:"))
        if p==a:
            k.balance()
        elif p==b:
            k.balanc()
        elif p==c:
            k.balan()
        elif p==d:
            k.bala()
        else:
            print("please,check your account number.")
    if ch==2:
        p=int(input("ENTER YOUR ACCOUNT NUMBER:"))
        if p==a:
            k.withdraw()
        elif p==b:
            k.withdra()
        elif p==c:
            k.withdr()
        elif p==d:
            k.withd()
        else:
            print("please,check your account number.")
    if ch==3:
        break
del b

            
