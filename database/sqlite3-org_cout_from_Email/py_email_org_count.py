import sqlite3
conn=sqlite3.connect("emaildb.sqlite")
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
try:
    fhand=open(input("enter the emails file:"))
except:
    fhand=open('mbox.txt')
    
for line in fhand:
           if line.startswith("From:"):
               a=line.split()
               email=a[1]
               #print(a[1])
               orga=email.split("@")[1]
               cur.execute('SELECT org FROM counts WHERE org=?',(orga,))
               row=cur.fetchone()
               if row is None:
                   cur.execute('INSERT INTO counts(org,count) VALUES(?,1)',(orga,))
               else:
                   cur.execute('UPDATE counts SET count=count+1 WHERE org=?',(orga,))
conn.commit()
            
               
str="SELECT org,count FROM counts ORDER BY count"
for line in cur.execute(str):
    print(line)
               
              
                   
               
