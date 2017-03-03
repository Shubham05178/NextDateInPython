def next(d,m,y):
    if(y%400==0 or (y%4==0 and y%100!=0)):
        s=True
    else:
        s=False

    if(s==True and m==2 and d==28):
        print("The Next Date is 29-02-"+str(y))
        return
    if(s==True and m==2 and d==29):
        print("The Next Date is 01-03-"+str(y))
        return
    if(s==False and m==2 and d==28):
        print("The Next Date is 01-03-"+str(y))
        return
    if(m==2 and d>28 and s==False):
        print("Invalid date input")
        return
    if(m==2 and d>29 and s==True):
        print("Invalid date input")
        return
    if (m==12 and d==31):
        print("The Next Date is 01-01-"+str(y+1))
        return
    if(m==12 and d>31):
        print ("Invalid date input")
        return
    if((m==1 or m==3 or m==5 or m==7 or m==8 or m==10) and (d>31)):
        printf("Invalid date input")
        return
    if((m==4 or m==6 or m==9 or m==11 ) and d>30):
        printf("Invalid date input")
        return
    if((m==1 or m==3 or m==5 or m==7 or m==8 or m==10) and (d==30)):
        print("The Next Date is 31-"+str(m)+"-"+str(y))
        return
    if (d==30 or d==31):
        print("The Next Date is 01-"+str(m+1)+"-"+str(y))
        return
    else:
        print("The Next Date is "+str(d+1)+"-"+str(m)+"-"+str(y))
        return


d=input("ENTER YOUR DATE>>")
day,month,year=map(int,d.split('-'))
if(day>0 and month >0 and year >0):
    next(day,month,year)
else:
    print("Invalid date input")
