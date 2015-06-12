__author__ = 'Alxetraz'
def getIt():
    allCases=[]
    allCases=(raw_input().split())
    return allCases

def rev(case):
    newCase=''
    j=len(case)-1
    while j>=0:
        newCase+=case[j]
        j-=1
    return int(newCase)   
                 
def main():
    noCases=int(raw_input())
    for i in range(noCases):
        Tcases=getIt()
        no1=rev(Tcases[0])
        no2=rev(Tcases[1])
        final=no1+no2
        print((rev(str(final))))
        
main()