#------------------------Cab Booking---------------------------
import time
import cabModule
print('-------------Welcome to My Drive----------------')
while 1:
    print('''\n---Services---
1.Book my Drive
2.Exit''')
    ch=int(input('Enter your choice = '))
    if ch==1:
        name=input("Enter your name = ")
        while 1:
            ph=input("Enter your contact number = ")
            if ph.isdigit() and len(ph)==10:
               break
            print('Invalid Mobile number')
        while 1:
            dep=cabModule.Departure() 
            if dep<6 :
                break
            else:
                print('Invalid Choice')
        while 1:
            dest=cabModule.Destination() 
            if dest<6:
                break
            else:
                print('Invalid Choice')
        dep_point=cabModule.Departure_Point(dep)
        dest_point=cabModule.Destination_Point(dest)
        dist=cabModule.distance(dep,dest)
        cost=dist*10
        print('''\nYour Drive Booked
Name = {}
Phone Number = {}
From {} to {}
Total distance {}
Your Bill is {}\n'''.format(name,ph,dep_point,dest_point,dist,cost))  
        print(dep_point,end=' ') 
        for i in range(0,dist):
            print("-",end=' ')
            time.sleep(1)
        print(dest_point,end=' ') 
        print('\nYou reached your destination')
    elif ch==2:
        print('\nThank You........:)')
        break
    else:
        print('Invalid choice')