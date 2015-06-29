for t in xrange(input()):
    input()
    case=map(int,raw_input().split())
    sumT=0
    time=0
    for i in case:
        sumT+=i
        if sumT<0:
            time+=sumT
            sumT=0
    print "Scenario #"+str(t+1)+": "+str(abs(time)+1)+"\n"