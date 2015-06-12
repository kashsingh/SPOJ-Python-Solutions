'''
the formula for solving the problem is r=( (r1*r2*r3) / ( (r1*r2) + (r1*r3) + (r2*r3) +2* ( sqrt( (r1*r2*r3)*(r1+r2+r3) ))))  
where r is radius of circle required and r1, r1 & r3 are radius of respective given circles.
'''
        
def getIt():
    case=map(int,raw_input().split())
    return case

def main():
    noc=int(raw_input())
    for i in range(noc):
        case=getIt()
        r1=case[0]
        r2=case[1]
        r3=case[2]
        r=( (r1*r2*r3) / ( (r1*r2) + (r1*r3) + (r2*r3) +2.0*(((r1*r2*r3)*(r1+r2+r3))**0.5 )))         
        print "{:.6f}".format(r)

main()
