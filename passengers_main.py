from passengers import details

obj=details()

pid=int(input('Enter passenger Id :'))
pname=input('Enter passenger name :')
age=int(input('Enter your age:'))
mo_num=int(input('Enter your mobile number:'))
gender=input('Enter your gender:')

obj.insertdetails(pid,pname,age,mo_num,gender)