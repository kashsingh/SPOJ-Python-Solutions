while True:
    no=input()
    if no==0:
        break
    else:
        case=raw_input()
        i = 0
        newStr=''
        while i<=len(case)/no:
            if i%2==0:
                '''even case'''
                newStr+=case[i*no:(i+1)*no]
            else:
                '''odd case'''
                newStr+=(case[i*no:(i+1)*no])[::-1]
            i+=1
        ans=''
        i=0
        while i<no:
            j=i
            while j<len(newStr):
                ans+=newStr[j]
                j+=no
            i+=1
            
        print ans