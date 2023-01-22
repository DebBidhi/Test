t=['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]=['a','v']
print(t)

a=4
b=5
c=b+1
b=6
e=b+1
d=c+1
print(a,b,c,d,e)
if e==c:
    print("not sadowing")
else:
    print("shdowing")

def pow(x,y):
    if y==0:
        return 1
    else:
        return x*pow(x,y-1)
        

print(pow(2,3))

