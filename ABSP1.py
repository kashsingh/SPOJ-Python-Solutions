def getIt():
    allCases=[]
    noCases=int(raw_input())
    for i in range(noCases):
        no=int(raw_input())
        allCases.append(map(int,raw_input().split()))
    return allCases

def getDiff(case):
    SOD=0
    i=0
    while i<len(case):
        SOD+=i*case[i]-(len(case)-i-1)*case[i]
        i+=1
    return SOD
        
def main():
    Tcases=getIt()
    for case in Tcases:
        print(getDiff(case))    
    
main()
    
