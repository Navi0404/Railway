import mysql.connector


class book:
    def __init__(self):
        
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Navinash12345",
            database='Railwaysystem'
            )
        
    def trainfetch(self,src,dest):
        cur=self.conn.cursor()
        cur.execute(f'''select ROUTES.TRAIN_NO,SOURCE,STOP1,STOP2,STOP3,STOP4,DESTINATION FROM ROUTES INNER JOIN TRAIN_DETAILS ON
                    ROUTES.TRAIN_NO=train_details.TRAIN_NO
                    WHERE SOURCE='{src}' OR STOP1='{src}' OR STOP2='{src}' OR STOP3='{src}' OR STOP4='{src}';''')
            
        dt=cur.fetchall()

        try:
            tr=[]
            for i in dt:
                for j in i[i.index(src)+1:]:
                    if j==dest:
                        tr.append(i)
                        
        except:
            pass                
        if len(tr)==0:
            print('No Trains Available')
        else:
            print(tr)
     
     
    def addpassenger(self,pid,pname,age,mo_num,gender):
        self.cur=self.conn.cursor()
        self.cur.execute(f"INSERT INTO passengers VALUES ({pid},'{pname}',{age},{mo_num},'{gender}')")
        self.conn.commit()
        print('Passenger added sucessfully')    
        
        
    def addtransaction(self,tid,pid,fare,payment_mode):
        self.cur=self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRANSACTIONS VALUES ({tid},{pid},{fare},'{payment_mode}')")
        self.conn.commit()
        print('Transaction done sucessfully')   
        
    def bookticket(self,booking_id,pid,cls,seat_no,tid,source,dest,train_no):
        self.cur=self.conn.cursor()
        self.cur.execute(f"INSERT INTO BOOK_TICKETS VALUES ({booking_id},{pid},'{cls}',{seat_no},{tid},'{source}','{dest}',{train_no})")
        self.conn.commit()
        print('Ticket has been booked sucessfully')         
        print(pid,seat_no,booking_id,cls,source,dest,train_no,tid)
    




    
    
        
    