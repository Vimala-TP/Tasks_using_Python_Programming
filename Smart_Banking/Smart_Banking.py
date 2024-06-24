#----------Smart Banking-----------
class A():
    def credit(self,bal,pin):
        while 1:
            try:
                cr=float(input("Enter amount to Credit = "))
                break
            except ValueError as e:
                print("Invalid input...",e)
        while 1:
            epin=input("Enter your PIN = ")
            if epin!=pin:
                print("Incorrect PIN")
            else:
                print(cr," amount is Credited")
                bal+=cr
                break
        return bal
    def debit(self,tde,bal,pin):
        while 1:
            while 1:
                try:
                    de=float(input("Enter amount to Debit = "))
                    break
                except ValueError as e:
                    print("Invalid input...",e)
            if(de<=bal and tde<=100000.0):
                while 1:
                    epin=input("Enter your PIN = ")
                    if epin!=pin:
                        print("Incorrect PIN")
                    else:
                        print(de," amount is Debited")
                        tde+=de
                        bal-=de
                        break
                break
            if(de>bal or bal==0):
                print("Insufficient Balance")
                break
            if(tde>100000.0):
                print("Limit Exceeded\nPer day the limit is 100000")
                bal+=de
                break
        return tde,bal
bal=0.0
cr=0.0
tde=0.0
c=0
print("\n-------------------------SMART BANKING-------------------------\n")
while 1 :
    print('''\n1.Create an Account
2.To Login to the Account
3.To Exit''')
    try:
        ch=int(input("Enter your choice = "))
    except Exception as e:
        print("Invalid choice...",e)
    if(ch==1):
        if c==2:
            print("\nYou have already created the account")
        else:
            c=1
            print("\n-----Page to Create an Account-----\n")
            accn=input("Enter Bank Account Number = ")
            ifsc=input("Enter IFSC code = ")
            name=input("Enter Account Holder Name (Minimum 5 charachter) = ")
            l=len(name)
            while l<5:
                name=input('''Invalid Account Holder Name...!
    ReEnter Account Holder Name (Minimum 5 charachter) = ''')
                l=len(name)
            brch=input("Enter Branch Name = ")
            while 1:
                print('''\nEnter the type of plan you open an account
    1.Zero Account
    2.Student Account
    3.Bussiness account''')
                ch1=int((input("Enter your choice = ")))
                if ch1==1:
                    acctype="Zero Account"
                    break
                elif ch1==2:
                    acctype="Student Account"
                    bal=500.0
                    break
                elif ch1==3:
                    acctype="Bussiness Account"
                    bal=1000.0
                    break
                else:
                    print("Invalid Choice")
            aid=accn
            pwd=name[0:2]+name[l-2:]
            print("\nCongrats...! Your Account Created")
            print('''User id = {}
Password = {}
Account Number = {}
IFSC = {}
Holder Name = {}
Branch Name = {}\n'''.format(aid,pwd,accn,ifsc,name,brch))
            while 1:
                pin=input("Enter PIN to create(Exactly 6 numbers) = ")
                if len(pin)==6 and pin.isdigit():
                    print("Congrats your PIN is created")
                    c=2
                    break
                else:
                    print("Invalid PIN.....")
    elif(ch==2):
        if c==0:
            print("\nFirst you have to create an account")
        else:
            print("\n-----Login Page-----\n")
            while 1:
                lid=input("Enter your id = ")
                lp=input("Enter your Password = ")
                if lid!=aid or lp!=pwd :
                    print("\nInvalid id or Password....ReEnter id and password...")
                else:
                    break
            while 1:
                print("Your Bank Balance is ",bal)
                print('''\n1.Credit
2.Debit
3.Exit''')
                ch2=int(input("Enter your choice = "))
                o1=A()
                if ch2==1 :
                    bal=o1.credit(bal,pin)
                elif ch2==2 :
                    tde,bal=o1.debit(tde,bal,pin)
                elif ch2==3:
                    break
                else:
                    print("Invalid Choice")
    elif(ch==3):
        print("\nThank You...:)")
        break
    else:
        print("\nInvalid Choice\n")         
