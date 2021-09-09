#!C:\Users\Vvaibhav\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type: text/html")
print()

import cgi

form = cgi.FieldStorage()
se =  form.getvalue('software_value')

#print("<h1>Form Data : "+ se)

key = se

print("""<html>
            <head>
            <title> Result </title></head>
            <body>""")

print("<center style='color:red; font-size : 40px; font-family:monospace; border: 5px solid gray; border-radius: 10px;'>"+"You Have Entered : "+ key+"</center>")
print("<br>")

key = se.lower()

import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="database1"
)

c=mydb.cursor()
lens=len(key)

#a=key[0]+'%'
if lens > 3:
    a=key[0:int(lens/2)+1]+'%'
else:
    a=key+'%'
    
c.execute("select * from softwares where soft_names like '%s' " %a)

result = c.fetchall()

count = 0
c = key

def fun(a):
    if a == lens:
        print("<br> >>>")
        print(r[0])
        print("<br>")
        print("<a href='"+r[1]+"'>"+r[1]+"</a><br>")
    print("<br>")
    count = 0
    return;


print("<center style='color:red; font-size : 20px; font-family:monospace; border: 5px solid gray; border-radius: 10px;'>")
for r in result:
#    i += 1 
	for a in r:
		for char in a:
			for c in key:
				if c == char and count < lens:
					count += 1
					break
	fun(count)

print("</center>")
#	if count == lens:
#		print("<h1>"+r)
#	count = 0

mydb.commit()
mydb.close()

print("""</body>
            </html>""")

