noOfCase=int(raw_input())
blank=raw_input()
for i in range(noOfCase): 
    noOfStudent=int(raw_input())
    totalCandy=0
    for j in range(noOfStudent):
        totalCandy+=int(raw_input())
    if totalCandy%noOfStudent==0:
        print "YES"
    else:
        print"NO"
    if i+1==noOfCase:
        break
    else:
        blank=raw_input()