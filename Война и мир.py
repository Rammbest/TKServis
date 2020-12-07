massiv=[i.lower() for i in input().split()]
spisok={}
kolichestvo=1
for element_dlya_obhoda in massiv:
    if element_dlya_obhoda not in spisok:
        for element_dlya_sravneniya in massiv:
            if element_dlya_obhoda==element_dlya_sravneniya:
                if element_dlya_obhoda in spisok:
                    spisok[element_dlya_obhoda]+=kolichestvo
                else:
                    spisok[element_dlya_obhoda]= kolichestvo

for k,v in spisok.items():
    print(k,v)
