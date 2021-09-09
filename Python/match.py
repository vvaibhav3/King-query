import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="database1"
)

c=mydb.cursor()


key=input("enter a key :")

lens=len(key)

#print(key[0])

#sql = "select * from demo where movie_name like (?)",(key)
a=key[0]+'%'
c.execute("select game_names from games where game_names like '%s' " %a)

result = c.fetchall()

count = 0
c=key

def fun(k):
    print(k)
    return;

for r in result:
#	print(r)
	for a in r:
		for char in a.lower():
			#print(char)
			for c in key:
				#print(c)
				if c == char and count < lens:
					count += 1
					break			#break
    fun(a)  
#if count == lens and key == trim:
#    print(r)
    count = 0
	


mydb.commit()
mydb.close()
