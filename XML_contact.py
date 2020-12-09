# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse('fh.xml', parser=parser)
root = tree.getroot()
spisok = {}
name = ''
for elem in root:
    for subelem in elem:
        for subsubelem in subelem:
             if subsubelem.text!= None:
                if len(subsubelem.text)> 12 and subsubelem.text[:4]!="3743":# and subsubelem.text[:-1]!=".":
                    name = subsubelem.text
                elif len(subsubelem.text)==3 and subsubelem.text!='SIP' and subsubelem.text[-1]!='.':
                    spisok[name] = subsubelem.text

print(spisok)

contacts = ET.Element('contacts')
i=0
for key,val in spisok.items():
    i+=1
    contact = ET.SubElement(contacts, 'contact')
    contact.set("number",str(i))
    contact.set("name", key)
    contact.set("firstname", '')
    contact.set("lastname", '')
    contact.set("phone", val)
    contact.set("mobile", '')
    contact.set("email", '')
    contact.set("address", '')
    contact.set("city", '')
    contact.set("state", '')
    contact.set("zip", '')
    contact.set("comment", '')
    contact.set("presence", '')
    contact.set("info", '')
appt = open('appt.xml','w',encoding="utf-8")
strET = ET.tostring(contacts,encoding="utf-8")
strET= strET.decode(encoding="utf-8", errors="strict")
appt.write(strET)
