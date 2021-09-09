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
if lens > 3:
    a=key[0:int(lens/2)]+'%'
else:
    a=key+'%'
    
c.execute("select * from games where game_names like '%s' " %a)

result = c.fetchall()

count = 0
c=key

#if lens > 3:
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
    #	print(count)
    if count == lens:
        print(r)
    count = 0
#else:
#    for r in result:
#    #	print(r)
#        for a in r:
#            for char in a.lower():
#                #print(char)
#                for c in key:
#                    #print(c)
#                    if c == char and count < lens:
#                        count += 1
#                        break			#break
#    #	print(count)
#        if count == lens:
#            print(r)
#        count = 0

mydb.commit()
mydb.close()
