def getIt():
    line=raw_input()
    symbol='+-*'
    for i in line:
        if i in symbol:
            int1=int(line[:line.index(i)])
            int2=int(line[line.index(i)+1:])
            op=i
    case=[]
    case.append(int1)
    case.append(int2)
    case.append(op)
    return case
    
    
def addsub(case):
    if case[2]=='+':
        total=case[0]+case[1]
    else:
        total=case[0]-case[1]
    lenre=len(str(total))
    len1=len(str(case[0]))
    len2=len(str(case[1]))
    reference=max(lenre,len1,len2+1)
    print(' '*(reference-len1)+str(case[0]))
    print(' '*(reference-len2-1)+case[2]+str(case[1]))
    print(' '*(reference-lenre)+ "-"*(lenre))
    print(" "*(reference-lenre)+str(total)+'\n')
        
        
def mul(case):
    result=case[0]*case[1]
    lenre=len(str(result))
    len1=len(str(case[0]))
    len2=len(str(case[1]))
    ref=max(lenre,len1,len2+1)
    sp1=ref-len1
    sp2=ref-len2-1
    sp3=ref-lenre
    print(' '*sp1+str(case[0]))
    print(' '*sp2+case[2]+str(case[1]))
    if len2==1:
        print('-'*ref)
        print(' '*sp3+str(result)+'\n')
        
    else:
        refDash1=len2+1
        spD1=ref-refDash1
        print(' '*spD1+"-"*refDash1)
        i=0
        while i<len2:
            tempRe=case[0]*int(str(case[1])[len2-i-1])
            tempLe=len(str(tempRe))
            tempSp=ref-tempLe-i
            print(" "*(tempSp)+str(tempRe))
            i+=1
        spD2=ref-lenre
        print(" "*spD2+"-"*lenre)
        print(" "*spD2+str(result)+'\n')        
    
    
def main():
    noOfCases=int(raw_input())
    for i in range(noOfCases):
         case=getIt()
         if case[2]=='+' or case[2]=='-':
             addsub(case)
         else:
             mul(case)
        
main()