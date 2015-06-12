noofCases=int(raw_input())
case=[]
for i in range(noofCases):
    case.append(int(raw_input()))
    
sortedCase=sorted(case)
Tsum=0
for i in case:
    Tsum+=i
avgload=Tsum/2
i=0
lhand=0
answer=[]
while i < noofCases:
    if lhand>=avgload:
        break
    else:
        lhand+=sortedCase[i]
        answer.append(case.index(sortedCase[i])+1)
    i+=1

answer.sort()
for i in answer:
    print(i)