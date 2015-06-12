def getIt():
    Tot=int(raw_input())
    y=int(raw_input())
    case=[]
    case.append(Tot)
    case.append(y)
    return case
    
def main():
    i=0
    while i<10:
        case=getIt()
        x=(case[0]-case[1])/2
        print x+case[1]
        print x
        i+=1   
main()