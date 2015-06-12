def getIt():
    allCases=[]
    while True:
        try:
            case=raw_input()
        except:
            break
        
        i=0
        while i <len(case):
            if case[i]=='(':
                start=i
            elif case[i]==',':
                mid=i
            elif case[i]==')':
                end=i
                break
            i+=1
            
        X=float(case[start+1:mid])
        Y=float(case[mid+1:end])
        coordinates=[X,Y]
        allCases.append(coordinates)
    return allCases

def printIt(c1,c2,disTravelled):
    distance=((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**0.5
    newDisTravelled=distance+disTravelled
    print("The salesman has traveled a total of %0.3f kilometers.")%(newDisTravelled) 
    return newDisTravelled

def main():
    allCases=getIt()
    distance=0
    i=0
    
    while i<len(allCases)-1:
        distance=printIt(allCases[i],allCases[i+1],distance)
        i+=1


main()