from Book_tickets import details

obj=details()


booking_id=int(input('Enter booking_id :'))
pid=int(input('Enter passenger Id :'))
classs=input('Enter your Class:')
seat_no=int(input('Enter your seat_no :'))
tid=int(input('Enter Transcation id:'))
source=input('Enter your source :')
destination=input('Enter your destination:')
train_no=int(input('Enter your Train_no:'))


obj.insertdetails(booking_id,pid,classs,seat_no,tid,source,destination,train_no)