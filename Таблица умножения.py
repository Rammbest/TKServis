c = int(input())
d = int(input())
a = int(input())
b = int(input())
j = str("")
i = str("")
ai = a
aj = a
if a<=10 and b<=10 and c<=10 and d<=10 and a<=b and c<=d:
    while ai <= b:
        i += str(ai) + "\t"
        ai += 1
    print(""+"\t"+i)
    while c<=d:
        while aj<=b:
            j += "\t"+ str(c * aj) + "\t"
            aj += 1
        print(str(c) + j)
        c+=1
        aj = a
        j = ""
else:
    print("Error")