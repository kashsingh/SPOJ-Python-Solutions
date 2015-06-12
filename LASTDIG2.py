def lastDig(a,b):
    if b==0:
        return 1
    if b<=4:
        lastDigit=str(a**b)[-1]
        return lastDigit
    else:
        if b%4==0:
            return lastDig(a,4)
        else:
            return lastDig(a,b%4)
            

noOfCases=int(raw_input())
for i in range(noOfCases):
    case=raw_input().split()
    power=int(case[1])
    lastD=(case[0][-1])
    print lastDig(int(lastD),power)