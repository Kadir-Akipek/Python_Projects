import re

data = open("data.txt") 
oku = data.read() 

mail_listesi = re.findall("\S+@\S+",oku) 
print(mail_listesi)