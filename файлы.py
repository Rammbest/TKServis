import os
def access_file(file_name,mode,text_write=''):
    file = os.path.join("C:\python", file_name)
    with open (file,mode) as text:
        if mode=="r":
            str = text.readline().strip()
            return (str)
        elif mode=="w":
            text.write(text_write)

def calculation(str):
    spisok,integ,str_abc = [],'',''
    for i in str:
        if not i.isnumeric():
            if integ != '':
                spisok[-1] = spisok[-1] * int(integ)
            spisok.append(i)
            integ = ''
        else:
            integ += i
    spisok[-1] = spisok[-1] * int(integ)
    for i in spisok:
        str_abc += i
    return (str_abc)
file_name = input()
text_read = access_file(file_name,"r")
text_write = calculation(text_read)
access_file(file_name,"w",text_write)