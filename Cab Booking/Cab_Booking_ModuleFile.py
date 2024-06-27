def Departure():
    print('''\nSelect your Departure Point
1.V V Nagar
2.Kuvempu nagar
3.Kapugal Road
4.Talur Road
5.Aishwarya Colony''')   
    dep=int(input('='))   
    return dep
def Destination():
    print('''\nSelect your Departure Point
1.New Bustand
2.V V Nagar
3.Moti Circle
4.Devi Nagar
5.Sadhashiva Nagar''')   
    dest=int(input('='))  
    return dest
def Departure_Point(dep):
    Departure=["V V Nagar",'Kuvempu nagar','Kapugal Road','Talur Road','Aishwarya Colony']
    dl=len(Departure)
    for i in range(0,dl):
        if (dep-1)==i:
            dep_point=Departure[i]
            break
    return dep_point
def Destination_Point(dest):
    Destination=['New Bustand','V V Nagar','Moti Circle','Devi Nagar','Sadhashiva Nagar']
    dll=len(Destination)
    for i in range(0,dll):
        if (dest-1)==i:
            dest_point=Destination[i]
            break
    return dest_point
def distance(dep,dest):
    if dep==1 and dest==1:
        dist=15
    if dep==1 and dest==2:
        dist=20
    if dep==1 and dest==3:
        dist=25
    if dep==1 and dest==4:
        dist=19
    if dep==1 and dest==5:
        dist=10
    if dep==2 and dest==1:
        dist=23
    if dep==2 and dest==2:
        dist=12
    if dep==2 and dest==3:
        dist=28
    if dep==2 and dest==4:
        dist=20
    if dep==2 and dest==5:
        dist=18
    if dep==3 and dest==1:
        dist=17
    if dep==3 and dest==2:
        dist=30
    if dep==3 and dest==3:
        dist=31
    if dep==3 and dest==4:
        dist=34
    if dep==3 and dest==5:
        dist=40
    if dep==4 and dest==1:
        dist=38
    if dep==4 and dest==2:
        dist=39
    if dep==4 and dest==3:
        dist=42
    if dep==4 and dest==4:
        dist=45
    if dep==4 and dest==5:
        dist=18
    if dep==5 and dest==1:
        dist=15
    if dep==5 and dest==2:
        dist=15
    if dep==5 and dest==3:
        dist=15
    if dep==5 and dest==4:
        dist=15
    if dep==5 and dest==5:
        dist=15
    return dist