n=input()
army1=map(int,raw_input().split())
army2=map(int,raw_input().split())
army1.sort()
army2.sort()
i=0
j=0
win=0
while(i<n and j<n):
    if(army1[i]<army2[j]):
        win+=1
        i+=1
        j+=1
    elif(army1[i]==army2[j]):
        j+=1
    else:
        j+=1
        
print win