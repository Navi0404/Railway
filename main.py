from Traindetails import details
from Train_capacity import capacity
from routes import routes
from Book_tickets import book
import numpy as np

#Heading For the Project Railway management System

print("-"*10,"Welcome To Railway Management Sysytem","-"*10)


print("-"*5,"For Inserting the Data Enter - 1 :","-"*5)
print("-"*5,"For Reading the Data Enter - 2 :","-"*5)
print("-"*5,"For Updating the Data Enter - 3 :","-"*5)
print("-"*5,"For Deleting the Data Enter - 4 :","-"*5)

opr=int(input("Please Enter your operation :"))

if opr==1:
    print('--- For Inserting the data in traindetails press 1---')
    print('--- For Inserting the data in traincapacity press 2 ---')
    print('--- For Inserting the data in routes press 3 ---')
    print('--- For Booking the ticket press 4 ---')
    
    inopr=int(input('Please Select an operation :'))
    if inopr==1:
        obj=details()

        tno=int(input('Please Enter train no :'))
        src=input('Please Enter Source station :')
        dst=input('Please Enter Destination station :')
        tname=input('Please Enter Train name :')   

        obj.insertdetails(tno,src,dst,tname)

    if inopr==2:
        
        obj=capacity()
        obj1=details()
        obj1.trainfetch()

        train_no=int(input('Enter Train no:'))
        ac_1=int(input('Enter capacity ac_1 no:'))
        ac_2=int(input('Enter capacity ac_2 no:'))
        ac_3=int(input('Enter capacity ac_3 no:'))
        sl=int(input('Enter capacity Sl no:'))
        genral=int(input('Emter capacity genral no:'))


        obj.insertdetails(train_no,ac_1,ac_2,ac_3,sl,genral)
        
    if inopr==3:
        
        obj2=routes()
        obj1=details()
        obj1.trainroutes()

        train_no=int(input('Enter Train_no :'))
        stop_1=input('Enter stop_1:')
        stop_2=input('Enter stop_2:')
        stop_3=input('Enter stop_3:')
        stop_4=input('Enter stop_4:')


        obj2.routesinsert(train_no,stop_1,stop_2,stop_3,stop_4)
   
    if inopr==4:
        source=input('From :')
        dest=input('To :')
        obj=book()
        obj.trainfetch(source,dest)
        train_no=int(input('Enter Train no :'))
        cls=input('Please enter your coach :')
        
        #passenger 
        pid=int(input('Enter passenger Id :'))
        pname=input('Enter passenger name :')
        age=int(input('Enter your age:'))
        mo_num=int(input('Enter your mobile number:'))
        gender=input('Enter your gender:')
        
        obj.addpassenger(pid,pname,age,mo_num,gender)
        
        #Transaction
        tid=int(input('Enter Transcation id:'))
        pid=int(input('Enter passenger id:'))
        fare=int(input('Enter fare:'))
        payment_mode=input('Enter payment_mode:')
        
        obj.addtransaction(tid,pid,fare,payment_mode)
        
        #Booking ticket
        booking_id=np.random.randint(0,500000,1)[0]
        seat_no=np.random.randint(0,500000,1)[0]
        
        obj.bookticket(booking_id,pid,cls,seat_no,tid,source,dest,train_no)
        

        
        
        
        
        
             
if opr==3:
    pass
if opr==4:
    pass
