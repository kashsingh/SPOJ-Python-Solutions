def getit():
    allcases=[]
    try:
        while True:
             t=map(int,raw_input().split())
             allcases+=t
    except:
        pass
        
    allcases=sorted(allcases)
    return allcases
    
def main():
    cases=getit()
    i=cases[0]
    t=0
    j=cases[0]
    while t<len(cases):
        if not cases[t]==cases[t-1]+1 and t>0:
            j=cases[t-1]
            print ("for (int i = "+ str(i)+ "; i <= " + str(j)+ "; i++) cout << i << \" \";")
            i=cases[t]
        if t==len(cases)-1:
            j=cases[t]
            print ("for (int i = "+ str(i)+ "; i <= " + str(j)+ "; i++) cout << i << \" \";") 
        t+=1
    

if __name__ == "__main__":
    main()
        
        