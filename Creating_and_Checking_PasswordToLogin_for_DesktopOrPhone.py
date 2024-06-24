#----------------------------Password Checking-------------------------------
import time
print("------------Welcome------------")
while(1):
    print("\n1.Set Password to Desktop")
    print("2.Set Password to Phone")
    print("3.Exit")
    c=int(input("Enter your choice="))
    if(c==1):
        cp=input("\nEnter a password to create=")
        print("congrats...! Your Password is created as ",cp)
        lcp=len(cp)
        if(lcp==len(cp)):
            u1=input("\nEnter a password to login U1=")
            if(cp==u1 and lcp==len(u1)):
                print("---Welcome to Home U1 :)---")
            else:
                print("Incorrect Password / Length of password is different")
                while(cp!=u1) : 
                    for i in range(0,5):
                        u1=input("\nRe-Enter a password to login U1=")
                        if(cp==u1):
                            print("---Welcome to Home U1 :)---")
                            break
                        print("Incorrect Password / Length of password is different")
                    if(cp!=u1):
                          print("\nThis Device is locked. Try again in 30 seconds")
                          a=30
                          while a!=0 :
                              print(a)
                              time.sleep(1)
                              a-=1

    elif(c==2):
        cp=input("\nEnter a password to create=")
        llcp=len(cp)
        if(llcp==8):
            print("Congrats...!Your new Password is ",cp)
            u2=input("\nEnter a Password to Login U2=")
            if(cp==u2 and llcp==len(u2)):
                print("---Welcome to Home U2 :)---")
            else:
                print("Incorrect password / Length of password is different")
                while(cp!=u2) : 
                    for i in range(0,5):
                        u2=input("\nRe-Enter a password to login U2=")
                        if(cp==u2 and llcp==len(u2)):
                            print("---Welcome to Home U2 :)---")
                            break
                        print("Incorrect Password / Length of password is different")
                    if(cp!=u2):
                          print("\nThis Device is locked. Try again in 30 seconds")
                          a=30
                          while a!=0 :
                              print(a)
                              time.sleep(1)
                              a-=1
        else:
            print("Password is limited to 8 digits")
    elif(c==3):
        print("\n-----Thank You :)-----")
        break
    else:
        print("Enter a valid choice")
