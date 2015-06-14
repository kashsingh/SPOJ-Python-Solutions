t=input()
for i in range(t):
    m=raw_input()
    case=raw_input().split()
    j=0
    while j<len(case):
        if "machula" in case[j]:
            no=j
        j+=2
    
    if no==0:
        miss=int(case[4])-int(case[2])
    elif no==2:
        miss=int(case[4])-int(case[0])
    else:
        miss=int(case[0])+int(case[2])
    
    case[no]=str(miss)
    print case[0]+" "+case[1]+" "+case[2]+" "+case[3]+" "+case[4]