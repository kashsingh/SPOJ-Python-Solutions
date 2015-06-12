def getIt():
    allCases=[]
    while True:
        lenght=int(raw_input())
        if lenght==0:
            break
        else:
            case=(raw_input().split())
            i=0
            while i<len(case):
                case[i]=int(case[i])
                i+=1
            allCases.append(case)
    return allCases

def inverseTest(case):
    ambi=True
    i=0
    while i<len(case):
        i+=1
        if case[case[i-1]-1]==i:
            continue
        else:
            ambi=False 
            break
        
    if ambi==True:
        print'ambiguous'
    else:
        print'not ambiguous'
          

Tcases=getIt()
for case in Tcases:
    inverseTest(case)
    