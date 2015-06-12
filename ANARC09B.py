def gcd(a,b):
        while b: a, b = b, a%b
        return a
        
def lcm(a,b):
    return (a*b)/gcd(a,b)
    
def main():
    while True:
        l1=map(int,raw_input().split())
        a=l1[0]
        b=l1[1]
        if a==0 and b==0:
            break
        else:
            print(lcm(a,b)/gcd(a,b))
    
main()