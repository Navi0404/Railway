from Traindetails import details

obj=details()

tno=int(input('Please Enter train no :'))
src=input('Please Enter Source station :')
dst=input('Please Enter Destination station :')
tname=input('Please Enter Train name :')   

obj.insertdetails(tno,src,dst,tname)