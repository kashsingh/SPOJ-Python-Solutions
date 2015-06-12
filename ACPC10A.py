while True:
    case=map(int,raw_input().split())
    if case[0]==case[1]==case[2]==0:
        break
    else:
        if case[1]-case[0]==case[2]-case[1]:
            N=2*case[2]-case[1]
            print 'AP '+str(N)
        else:
            N=case[2]**2/case[1]
            print "GP "+str(N)