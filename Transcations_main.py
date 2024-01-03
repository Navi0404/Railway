from Transcations import details

obj=details()

tid=int(input('Enter Transcation id:'))
pid=int(input('Enter passenger id:'))
fare=int(input('Enter fare:'))
payment_mode=input('Enter payment_mode:')

obj.insertdetails(tid,pid,fare,payment_mode)