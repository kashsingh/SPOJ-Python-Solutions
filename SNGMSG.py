def getIt():
    case=[]
    case.append(raw_input())
    case.append(raw_input())
    return case
    
def decode(case):
    key=case[0]
    message=case[1]
    dict1={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    dict2={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    newKey=key+key[::-1]
    lenMessage=len(message)
    lenNewKey=len(newKey)
    if lenNewKey<lenMessage:
        newKey*=(lenMessage/lenNewKey+1)
    i=0
    deMessage=[]
    while i<lenMessage:
        value=dict1[message[i]]
        diff=int(newKey[i])
        newValue=value-diff
        if newValue>=1:
            deMessage.append(dict2[newValue])
        else:
            deMessage.append(dict2[26+newValue])
        i+=1
    newMessage=''.join(deMessage)
    print(newMessage)  
        
        
def main():
    noOfCase=int(raw_input())
    for i in range(noOfCase):
        case=getIt()
        decode(case)

main()