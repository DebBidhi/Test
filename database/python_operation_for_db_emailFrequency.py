import sqlite3
conn=sqlite3.connect('db_using_python_operation.db')
cur=conn.cursor()
#'''
cur.execute('DROP TABLE IF EXISTS counts')

cur.execute('CREATE TABLE counts(email TEXT,count INTEGER)')
try:
    fh=open(input("enter file name:"))
except:
    fh=open('mbox.txt')
for line in fh:
    if not line.startswith("From:"): continue
    f=line.split()
    emailaddress=f[1]
    #print(type(emailaddress))
    cur.execute('SELECT email FROM counts WHERE email=?',(emailaddress,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO counts(email,count) values(?,1)',(emailaddress,))
    else:
        cur.execute('UPDATE counts SET count=count+1 where email=?',(emailaddress,))

conn.commit()
#'''
#once table is created the main operation can be done without th #''' body -#'''

sqlstr='SELECT email,count FROM counts'

for line in cur.execute(sqlstr):
    print(line)
    #print("the email is:",line[0])

    
cur.execute("SELECT email from counts")
etuple=cur.fetchall()
sum=len(etuple)
print("the total unique emails are:",sum)
cur.execute("SELECT count from counts")
etuple=cur.fetchall()
#print(etuple)#output--[(1,), (1,), (2,), (1,), (1,), (1,), (1,), (2,), (3,), (1,), (1,), (1,), (1,), (1,), (1,), (1,)]
a=0
for line in etuple:
    for no in line:
        a=a+int(no)

print("the sum of all count is:",a)



    
    
    
    
    
        
        

