#Code for Lift for 5 Floor0
import time
print("----------Welcome to Lift---------")
print("\nLift is present at Ground Floor")
f=0     #Default floor is 0 i.e Ground floor 
fl=["Ground floor","First floor","Second floor","Third floor","Fourth floor"]
while 1 :
    print("\n0 = Ground floor")
    print("1 = First floor")
    print("2 = Second floor")
    print("3 = Third floor")
    print("4 = Fourth floor")
    print("5 = Power Off the Lift")
    ch=int(input("Enter your Floor="))
#Way to Ground Floor
    if(ch==0):
        while f!=ch :
            print("\n",fl[f]," Departure")
            time.sleep(1)
            f-=1       
            print("\n",fl[f]," Arrieved")
            time.sleep(1)
        print("\nYou are at the ",fl[ch])
#Way to First Floor
    elif(ch==1):
        while(f!=ch):
            print("\n",fl[f]," Departure")
            time.sleep(1)
            if ch>f :
                f+=1
            else:
                f-=1
            print("\n",fl[f]," Arrieved")
            time.sleep(1)
        print("\nYou are at the ",fl[ch])
#Way to Second Floor
    elif(ch==2):
        while f!=ch:
            print("\n",fl[f]," Departure")
            time.sleep(1)
            if ch>f:
                f+=1
            else:
                f-=1
            print("\n",fl[f]," Arrieved")
            time.sleep(1)
        print("\nYou are at the ",fl[ch]) 
#Way to Third Floor
    elif(ch==3):
        if(f==4):
            print("\n",fl[f]," Departure")
            time.sleep(1)
            if ch>f:
                f+=1
            else:
                f-=1
            print("\n",fl[f]," Arrieved")
            time.sleep(1)
        print("\nYou are at the ",fl[ch])
#Way to Fourth Floor
    elif(ch==4):
        while f!=4 :
            print("\n",fl[f]," Departure")
            time.sleep(1)
            f+=1        
            print("\n",fl[f]," Arrieved")
            time.sleep(1)
        print("\nYou are at the ",fl[ch])
    elif(ch==5):
        print("\nLift is Offed")
        break
    else:
        print("\nInvalid floor number")