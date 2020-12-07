a = int(input())
b = int(input())
s,x = 0 , 0
if a%3==1:
    a+=2
elif a%3==2:
    a+=1
for j in range(a,b+1,3):
    s+=j
    x +=1
print(s/x)
