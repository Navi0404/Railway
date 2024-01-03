from routes import routes

obj=routes()

train_no=int(input('Enter Train_no :'))
stop_1=input('Enter stop_1:')
stop_2=input('Enter stop_2:')
stop_3=input('Enter stop_3:')
stop_4=input('Enter stop_4:')


obj.insertdetails(train_no,stop_1,stop_2,stop_3,stop_4)


