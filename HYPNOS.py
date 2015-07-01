n=raw_input()
count=0
while True:
    sq=0
    for i in n:
	sq+=int(i)**2
    count+=1
    n=str(sq)
    
    if len(n)==1:
        if int(n)==1:
            print count
            break
	else:
	   print "-1"
	   break
	       
    
