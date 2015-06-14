def answer(size,case):
    need=1
    status= True
    lane=[]
    for e in case:
        while(bool(len(lane)) and lane[-1]==need):
            need+=1
            lane.pop()
            
            
        if e==need:
            need+=1
            
        elif bool(len(lane)) and e>lane[-1]:
            status=False
            return status
            
        else:
            lane.append(e)
            
    return status
    
def main():
    while True:
        n=input()
        if n==0:
            break
        else:
            case=map(int,(raw_input().split()))
            
        if answer(n,case):
            print "yes"
        else:
            print "no"

main()