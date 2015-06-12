def getIt():
    allCases=[]
    noCases=int(raw_input())
    for i in range(noCases):
        allCases.append(map(int,raw_input().split()))
    return allCases

def fMul(case):
    x=case[0]
    y=case[1]
    power=len(str(min(x,y)))
    base=10**power
    x1=x/base
    x0=x%base
    y1=y/base
    y0=y%base
    z2=x1*y1
    z1=(x1+x0)*(y1+y0)-(x1*y1)-(x0*y0)
    z0=x0*y0
    result=z2*(base**2)+z1*base+z0
    return result
    
def main():
    Tcases=getIt()
    for case in Tcases:
        print(fMul(case))    
    
main()
    
