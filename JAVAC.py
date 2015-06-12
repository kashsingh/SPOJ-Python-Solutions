def convert(oStr):
    nStr=''
    L=len(oStr)
    cid=False
    jid=False
    
    if not oStr[0].isalpha():
        return "Error!"
        
    for i in oStr:
        if i.isupper():
            jid=True
            continue
        if i=="_":
            cid=True
        elif not i.isalpha():
            return "Error!"
        	
    if cid and jid:
        return "Error!" 
    
    if cid:
        if oStr[0]=='_' or oStr[-1]=='_':
            return "Error!"
            
        i=0        
        while(i<L):
            if (oStr[i]=='_' and not oStr[i+1]=='_'):
                nStr+=oStr[i+1].upper()
                i+=2
            elif(oStr[i]=='_' and oStr[i+1]=='_'):
                return "Error!"
            else:
                nStr+=oStr[i]
                i+=1
    else:
        if oStr[0].isupper():
            return "Error!"
        i=0        
        while(i<L):
            if (oStr[i].isupper()):
                nStr+='_'+oStr[i].lower()
            else:
                nStr+=oStr[i]
            i+=1   
    return nStr
                

def main():
    while True:
        try:
            oStr=raw_input()
            print convert(oStr)
        except:
            break
        
    

main()