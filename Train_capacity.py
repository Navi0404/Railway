import mysql.connector


class capacity:
    def __init__(self):
        
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Navinash12345",
            database='Railwaysystem'
            )
        
        
    def insertdetails(self,train_no,ac_1,ac_2,ac_3,sl,genral):
        self.cur=self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRAIN_CAPACITY VALUES ({train_no},'{ac_1}','{ac_2}','{ac_3}','{sl}','{genral}')")
        self.conn.commit()
        print('Data has been inserted sucessfully')            