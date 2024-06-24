#Python program for V-Mart billing
import time
import V_Mart_ModuleFile as Menu
def cost() :
    pass
g=["sugar","Rice","Dhall","Salt"]
k=["Spoons","Plates","Kitchen Towel","Cutting Board"]
c=["Jacket","T-Shirt","Towel","HandKerchief"]
qi=[0.0,0.0,0.0,0.0]
qk=[0.0,0.0,0.0,0.0]
qc=[0.0,0.0,0.0,0.0]
v=0
z=0
print("--------Welcome to V-Mart---------")
while 1:
    ch=Menu.ServiceMenu()
    if(ch==1):
        v=1                                                   
        while 1 :
            ch1=Menu.ShoppingMenu()
            if(ch1==1):
                while 1 :
                    ch11=Menu.GrocerryMenu()
                    if(ch11==1):
                        qii=float(input("Enter the quantity of Sugar in kg = "))
                        qi[0]+=qii
                    elif(ch11==2):
                        qj=float(input("Enter the quantity of Rice in kg = "))
                        qi[1]+=qj
                    elif(ch11==3):
                        qkk=float(input("Enter the quantity of Dhall in kg = "))
                        qi[2]+=qkk
                    elif(ch11==4):
                        ql=float(input("Enter the quantity of Salt in kg = "))
                        qi[3]+=ql
                    elif(ch11==5):
                        break
                    else:
                        print("Invalid item")
            elif(ch1==2):
                while 1 :
                    ch12=Menu.KitchenMenu()
                    if(ch12==1):
                        qm=float(input("Enter the quantity of  Spoons = "))
                        qk[0]+=qm
                    elif(ch12==2):
                        qn=float(input("Enter the quantity of Plates = "))
                        qk[1]+=qn
                    elif(ch12==3):
                        qo=float(input("Enter the quantity of Kitchen Towel = "))
                        qk[2]+=qo
                    elif(ch12==4):
                        qp=float(input("Enter the quantity of Cutting board = "))
                        qk[3]+=qp
                    elif(ch12==5):
                        break;
                    else:
                        print("Invalid item")
            elif(ch1==3):
                while 1 :
                    ch13=Menu.ClothesMenu()
                    if(ch13==1):
                        qq=float(input("Enter the total number of jakets = "))
                        qc[0]+=qq
                    elif(ch13==2):
                        qr=float(input("Enter the total number of T-Shirts = "))
                        qc[1]+=qr
                    elif(ch13==3):
                        qs=float(input("Enter the total number of Towels = "))
                        qc[2]+=qs
                    elif(ch13==4):
                        qt=float(input("Enter the total number of HandKerchiefs = "))
                        qc[3]+=qt
                    elif(ch13==5):
                        break;
                    else:
                        print("Invalid item")
            elif(ch1==4):
                break
            else:
                print("Invalid Choice")
    elif(ch==2):  
        if(v==0):
            print("\nFirst You have to do Shopping")
        else:
            z=1                                           #Verification Process
            print("\nAvailable Items among selected items are\n")
            u=0
            for i in qi :
                if g[u] in g:
                    if i>0.0 :
                        print(g[u]+" available\n")
                        time.sleep(1)
                u+=1
            u=0
            for i in qk :
                if k[u] in k:
                    if i>0.0 :
                        print(k[u]+" available\n")
                        time.sleep(1)
                u+=1
            u=0
            for i in qc :
                if c[u] in c:
                    if i>0.0 :
                        print(c[u]+" available\n")
                        time.sleep(1)
                u+=1
    elif(ch==3): 
          if(v==0):
              print("\nFirst You have to do Shopping")
          elif v!=0 and z==0:
              print("\nVerify the items before Billing")
          else:                                               
              print("\n----Billing Process----") 
              print("\nCustomer Details:")
              cname=input("Enter Customer name = ")
              cid=123
              cph=input("Enter Customer Contact number = ")
              while(1):
                  if(len(cph)==10 and cph.isdigit()):
                      break
                  cph=input('''Invalid Contact Number...!
ReEnter Customer Contact number = ''')

              print("\n------V-Mart-----\n-----Your Bill-----")
              v1=[40.0,50.0,60.0,30.0]
              v2=[60.0,100.0,80.0,220.0]
              v3=[1950.0,500.0,150.0,60.0]
              ci=[0.0,0.0,0.0,0.0]
              ck=[0.0,0.0,0.0,0.0]
              cc=[0.0,0.0,0.0,0.0]
              tcost=0.0
              u=0
              for i in qi:
                  ci[u]+=v1[u]*i            #Grocerry items cost calculating
                  u+=1
              u=0
              for i in qk:
                  ck[u]+=v2[u]*i            #Kitchen items cost calculating
                  u+=1
              u=0
              for i in qc:
                  cc[u]+=v3[u]*i             #Clothes items cost calculating
                  u+=1
              tcost=(ci[0]+ci[1]+ci[2]+ci[3]+ck[0]+ck[1]+ck[2]+ck[3]+cc[0]+cc[1]+cc[2]+cc[3])
              print("\nName: ",cname)
              print("ID: ",cid)
              print("Phone Number: ",cph)
              print("------------------------------------------------------------------")
              print("{:<20} {:<20} {:<20}".format("Items","Quantity","Cost"))
              print("------------------------------------------------------------------")
              u=0
              for i in qi :
                  if i>0.0 :
                      print("{:<20} {:<20} {:<20}".format(g[u],qi[u],ci[u]))
                  u+=1
              u=0
              for i in qk :
                  if i>0.0 :
                      print("{:<20} {:<20} {:<20}".format(k[u],qk[u],ck[u]))
                  u+=1
              u=0
              for i in qc :
                  if i>0.0 :
                      print("{:<20} {:<20} {:<20}".format(c[u],qc[u],cc[u]))
                  u+=1
              print("------------------------------------------------------------------")
              print("          Total Cost                      {}".format(tcost))
              print("------------------------------------------------------------------")
    elif(ch==4):
        print("\nThank You for Shopping :)")
        break
    else:
        print("Invalid Choice...!")
