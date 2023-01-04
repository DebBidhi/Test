#hname = input("enter file name:")


handle = open("hi.txt")
dic={
    "bidhideb@gmail.com":1,
    
    "bidhide@hotmail.com":3

}

for line in handle:
    a=line.split()
    #print(a)
    if line.startswith("From "):
        #print(a[1])
        dic[a[1]]=dic.get(a[1],0)+1
       

mail_no = max(dic.values())
max_key = max(dic, key=dic.get)



    

print(dic)
print(max_key)
print(mail_no)

print( max_key, mail_no)


