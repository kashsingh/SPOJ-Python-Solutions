'''The implementation of below code in C++ will give you AC but in Python it will give you TLE.'''
T = input()
for i in range(T):
    a=input()
    c=2**60
    b=a+1
    while(b<=2*a+1):
        if((a*b+1)%(b-a)==0):
	   c=min(c,b+(a*b+1)/(b-a))
        b+=1  
    print c