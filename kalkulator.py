a = int(input())
b = a%20
c = a%100%20
if a == 1 or b == 1 or c == 1:
    s = "st"
elif (b ==2 or b==3 or b==4) or (a ==2 or a==3 or a==4 )  or (c ==2 or c==3 or c==4 ):
    s = "sta"
# a//20%5!=0:
else:
    s="ov"
print(s)     
