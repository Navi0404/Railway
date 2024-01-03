import mysql.connector


class details:
    def __init__(self):
        
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Navinash12345",
            database='Railwaysystem'
            )
        
    
    def insertdetails(self,pid,pname,age,mo_num,gender):
        self.cur=self.conn.cursor()
        self.cur.execute(f"INSERT INTO passengers VALUES ({pid},'{pname}','{age}','{mo_num}','{gender}')")
        self.conn.commit()
        print('Data has been inserted sucessfully')    