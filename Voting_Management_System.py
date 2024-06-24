#--------------------VOTING SYSTEM-----------------------
def checkVotes(cp,c):
    cc=0
    m=max(c)
    for i in c:
        if i==m:
            cc+=1
    return cc
def voting(c,p,cp):
    candi=int(input("\nEnter total number of candidates = "))
    ic=0
    for i in range(0,candi):
        print('''\nWelcome candidate ''',ic+1)
        age=int(input("Enter your age = "))
        ic+=1
        if age<18:
            print('Not Eligible for Voting')
        else:
            print('''Enter your Vote''')
            icc=0
            for i in p:
                print('{}.{}'.format(icc+1,p[icc]))
                icc+=1
            ch=int(input('Enter your choice = '))
            for i in range(0,cp):
                if i==ch-1:
                    c[i]+=1
    return c
p=[]
c=[]
print('''\n------------------VOTING SYSTEM------------------\n
Arranging of parties\n''')
while 1:
    try:
        cp=int(input("Enter the count of Parties = "))
        break
    except Exception as e:
        print("Invalid Input...",e)
print('\nEnter Party Names')
ic=0
for i in range(0,cp):
    print('Enter Party ',ic+1,' Name')
    pn=input()
    ic+=1
    p.append(pn)
    c.append(0)
while 1:
    c=voting(c,p,cp)
    cc=checkVotes(cp,c)
    if cc==1:
        m=max(c)
        for i in range(0,cp):
            if m==c[i]:
                print('{} party is the Winner'.format(p[i]))   
        break
    else:
        print('\nReconduct Voting......Because a two parties got tie')