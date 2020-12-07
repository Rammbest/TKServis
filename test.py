a = []
b = []
c = {}
f = 0
for i in input():
    a += i
for j in input():
    b += j

while f < len(a):
    c[a[f]]=b[f]
    f+=1
str_code = input()
str_code2 = input()
shifr=''
shifr2=''
for s in str_code:
    shifr += c[s]

for s in str_code2:
    for k,v in c.items():
        if v == s:
            shifr2 += k
print(shifr)
print(shifr2)
