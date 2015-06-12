t=input()
for i in range(t):
    N,K,T,F=map(int,raw_input().split())
    result= N + (K*(F-N))/(K-1)
    print result