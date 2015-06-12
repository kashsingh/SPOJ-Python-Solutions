def getIt():
    testCases=int(raw_input())
    cases=[]
    for i in range(testCases):
        cases.append(int(raw_input()))
    return cases


def noOfZeroes(case):
    zeroes=0
    i=1
    while True:
        if (5**i)>case:
            break
        else:
            zeroes+=case/(5**i)
        i+=1
    return zeroes

    
Tcases=getIt()
for i in Tcases:
    assert(i<=1000000000),'Overflow'
    assert(i>=1),'Underflow'
    print(noOfZeroes(i))