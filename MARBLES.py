def getIt():
    case=[]
    case=(map(int,raw_input().split()))
    return case

def fact(case):
    if case==0:
        return 1
    elif case==1:
        return 1
    else:
        return case*fact(case-1)
        
def calculate(case):
    n=case[0]
    k=case[1]
    a=n-1
    b=k-1
    c=n-k
    i=max(b,c)
    afact=1
    while i<a:
        afact*=i+1
        i+=1
        
    result=afact/fact(min(b,c))
    print(result)
       
def main():
    noOfCases=int(raw_input())
    for i in range(noOfCases):
        case=getIt()
        calculate(case)
main()
