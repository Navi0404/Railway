import mysql.connector


class routes:
    def __init__(self):
        
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Navinash12345",
            database='Railwaysystem'
            )
        
        
    def routesinsert(self,train_no,stop_1,stop_2,stop_3,stop_4):
        self.cur=self.conn.cursor()
        self.cur.execute(f"INSERT INTO ROUTES VALUES ({train_no},'{stop_1}','{stop_2}','{stop_3 }','{stop_4}')")
        self.conn.commit()
        print('Data has been inserted sucessfully')