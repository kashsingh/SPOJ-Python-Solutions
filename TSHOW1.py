d = { 1:'5', 0: '6'}

def AMNO(N):
    ans=""
    while N:
	N,r = divmod(N,2)
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