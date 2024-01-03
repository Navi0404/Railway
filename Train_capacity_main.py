from Train_capacity import capacity

obj=capacity()

train_no=int(input('Enter Train no:'))
ac_1=int(input('Enter ac_1 no:'))
ac_2=int(input('Enter ac_2 no:'))
ac_3=int(input('Enter ac_3 no:'))
sl=int(input('Enter Sl no:'))
genral=int(input('Emter genal no:'))


obj.insertdetails(train_no,ac_1,ac_2,ac_3,sl,genral)