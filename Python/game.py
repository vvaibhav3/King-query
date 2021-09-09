#!C:\Users\Vvaibhav\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type: text/html")
print()

import cgi

form = cgi.FieldStorage()
se =  form.getvalue('game_value')

key = se

print("""<html>
            <head>
            <title> Result </title></head>
            <body>""")

print("""<style>
.v1{
text-align:center;
color:red; 
background-color:green;
font-size : 30px; 
font-family:monospace; 
border: 3px solid black;
border-bottom:1px solid white;
border-radius: 10px;
text-shadow : 2px 2px black;
width :30%;
 }
.v1:hover {
    text-align :center;
    background-color: white;
    color:black;
    font-weight:bold;
    text-shadow: none;
    box-shadow: 3px 4px black;
    width:40%;
    }
    
.v2{
color:red; 
font-size : 20px; 
font-family:monospace;
border: 3px solid green;
border-radius: 10px;
 }
.v2:hover{
border: 3px solid red;
box-shadow: 2px 4px black;
 }
</style>""")

print("<div class='v1'>"+"You Have Entered : "+ key+"</div>")


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
    
c.execute("select * from games where game_names like '%s' " %a)

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


print("<center><div class='v2'>")
for r in result:
#    i += 1 
	for a in r:
		for char in a:
			for c in key:
				if c == char and count < lens:
					count += 1
					break
	fun(count)

print("</div></center>")
#	if count == lens:
#		print("<h1>"+r)
#	count = 0

mydb.commit()
mydb.close()

print("""</body>
            </html>""")

