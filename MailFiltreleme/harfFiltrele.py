import re

x = "x şirketinin değeri  2003 yılında yllık $10000 dolar olurken, 2012 de $15000 dolara yükseldi"
y = re.findall("\$[0-9.]+",x) 
print(y)

x = "19 saat süren bir boyama festivalinde 10 tane rengin 28 farklı tonu kullanılmıştır."
y = re.findall("[0-9]+",x) 
print(y)

