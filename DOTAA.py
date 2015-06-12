def getIt(n,damage):
    health=[]
    for i in range(n):
        l=int(raw_input())
        if l>damage:
            health.append(l)
    
    return health
    
def calculate(health,damage,noOfTowers): 
    sum1=0
    if len(health)==0:
        return 'NO'
    for j in health:
        sum1+=j/damage 
    if sum1>=noOfTowers:
        return "YES"
    else:
        return "NO"
        
def main():
    noOfCases=int(raw_input())
    for i in range(noOfCases):
        line=[]
        line=map(int,raw_input().split())
        n=line[0]
        damage=line[2]
        noOfTowers=line[1]
        health=getIt(n,damage)
        print(calculate(health,damage,noOfTowers))
                    
        
main()