"""Same as TSHOW1 didn't even changed the code."""
d = { 4: 'k',3:'n',2:'a',1:'m',0:'u' }

def AMNO(N):
    ans=""
    while N:
	N,r = divmod(N,5)
	if r == 0:
	   N -= 1
	ans = d[r] + ans
    print ans
    
def main():
    t=input()
    for case in range(t):
        N=input()
        AMNO(N)

if __name__=="__main__":
    main()