noOfCases=input()
for i in range(noOfCases):
    case=map(int,raw_input().split())
    t=-1
    noOfAtoms=case[0]
    maxAtoms=case[2]
    if noOfAtoms<maxAtoms:
        while noOfAtoms<=maxAtoms:
            noOfAtoms*=case[1]
            t+=1 
        print t
    else:    
        print 0
        continue