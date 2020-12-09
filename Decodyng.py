# -*- coding: utf-8 -*-
appt = open('appt.xml','r').read()
# Декодируем из utf8 в unicode - из внешней в рабочую
# appt = appt.decode('utf8')
# Работаем с текстом
# appt += appt
# Кодируем тест из unicode в utf8 - из рабочей во внешнюю
appt = appt.encode('utf8')
# Сохраняем в файл с кодировкий utf8
open('appt.xml','w').write(appt)