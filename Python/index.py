#!C:\Users\Vvaibhav\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type: text/html")
print()

import cgi


print("<center><div class='v2' style='color:#f5f6fa;background-color:#2980b9; font-size : 40px; font-family:monospace;border-radius: 10px;text-shadow: 2px 4px black;border-bottom:2px solid #0097e6;'>"+" Latest Movies <div></center>")
print("""<style>
.v:hover{box-shadow: 1px 1.5px 1px 3px black;}
      </style>""")

import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="database1"
)

c=mydb.cursor()
    
c.execute("select * from latest")

result = c.fetchall()

print("<center><div class='v' style='color:#f5f6fa;background-color:#2980b9;font-size : 25px; font-family:monospace;border-radius: 10px;'>")
for r in result:
    print("<br>")
    print(r[0])
    print("<br>")
    print("<a href='"+r[1]+"' target='blank'>"+r[1]+"</a>")
#	for a in r:
#		for char in a:
#			for c in key:
#				if c == char and count < lens:
#					count += 1
#					break
#	fun(count)

print("</div></center>")
#	if count == lens:
#		print("<h1>"+r)
#	count = 0

mydb.commit()
mydb.close()

print("""</body>
            </html>""")

