h = int(input ())
b = h%4 == 0 and h%100!=0 or h%400 ==0
if  b:
    print ('Високосный')
else:
    print ('Обычный')
    
    

