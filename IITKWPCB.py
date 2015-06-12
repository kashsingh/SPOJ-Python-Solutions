from fractions import gcd

def main():
    noOfCase=int(raw_input())
    for i in range(noOfCase):
        case=int(raw_input())
        j=case/2
        maxCoprime=1
        while j>=2:
            if gcd(j,case)==1:
                maxCoprime=j
                break
            j-=1 
        print(maxCoprime)  
    
    
main()