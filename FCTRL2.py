def fact(case):
    if case==0:
        return 1
    elif case==1:
        return 1
    else:
        return case*fact(case-1)
        
testCases=int(raw_input())
cases=[]

for i in range(testCases):
    print(fact(int(raw_input())))

    