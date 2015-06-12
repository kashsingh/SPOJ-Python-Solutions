PI= 3.141592653589

def getIt():
    case=map(int,raw_input().split())
    return case

def main():
    while True:
        case=getIt()
        w=case[0]
        h=case[1]
        if w==0 and h==0:
            break
        r1=w/(2.0*PI)
        h1=h-(2.0*r1)
        r2=min(h/(2.0*PI+2),w/2.0)
        h2=w
        v1=PI*(r1**2)*h1
        v2=PI*(r2**2)*h2
        maxVol=max(v1,v2)
        print "{:.3f}".format(maxVol)
        
        

main()