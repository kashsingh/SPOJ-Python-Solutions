def getIt(testCase):
    allCases=[]
    for i in range(testCase*2):
        allCases.append((raw_input()).split())
    return allCases
    
def calculator(case):
    i=1
    result=0
    while i<len(case):
        if i==1:
            if case[i]=='+':
                result=int(case[i-1])+int(case[i+1])
            elif case[i]=='-':
                result=int(case[i-1])-int(case[i+1])
            elif case[i]=='*':
                result=int(case[i-1])*int(case[i+1])
            elif case[i]=='/':
                result =int(case[i-1])/int(case[i+1])
            elif case[i]=='=':
                result=int(case[i-1])
        else:
            if case[i]=='+':
                result+=int(case[i+1])
            elif case[i]=='-':
                result-=int(case[i+1])
            elif case[i]=='*':
                result*=int(case[i+1])
            elif case[i]=='/':
                result/=int(case[i+1])
        i+=2
    print(result)
    
def main():
    testCase=int(raw_input())
    Tcase=getIt(testCase)
    for i in Tcase:
        if len(i)>1:
            calculator(i)
        

main()