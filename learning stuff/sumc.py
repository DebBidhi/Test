import re
#without word boundries[it will only take all e.g 23,572  also a23f,b3 etc]
hand=open("sum.txt")


lst=list()
for line in hand:
    line.rstrip()
    stuff=re.findall('[0-9]+',line)
    #if len(stuff)<0: continue
    for no in stuff:
        lst.append(int(no))
        
print(sum(lst))
hand.close()

#with word boundries[it will only take e.g 23 572 1 not a23f,b23 etc]

hand=open("sum.txt")
lst=list()
for line in hand:
    line.rstrip()
    stuff=re.findall(r'\b[0-9]+\b',line)
    #if len(stuff)<0: continue
    for no in stuff:
        lst.append(int(no))
        
print(sum(lst))
hand.close()
 
