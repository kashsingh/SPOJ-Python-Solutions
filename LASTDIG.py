def getIt():
    testCases=int(raw_input())
    allCases=[]
    for i in range(testCases):
        allCases.append(map(int,raw_input().split()))
    return allCases

def lastDig(a,b):
    if b<=4:
        lastDigit=str(a**b)[-1]
        return lastDigit
    else:
        if b%4==0:
            return lastDig(a,4)
        else:
            return lastDig(a,b%4)
        
               
def main():
    Tcases=getIt()
    for case in Tcases:
        print(lastDig(case[0],case[1]))
        
main()