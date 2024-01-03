import mysql.connector


class details:
    def __init__(self):
        
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Navinash12345",
            database='Railwaysystem'
            )
        
    def insertdetails(self,tid,pid,fare,payment_mode):
        self.cur=self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRANSACTIONS VALUES ({tid},'{pid}','{fare}','{payment_mode}')")
        self.conn.commit()
        print('Data has been inserted sucessfully')        