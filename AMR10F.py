noOfCase=input()
for i in  range(noOfCase):
    N,A,D=map(int,raw_input().split())
    cookie=N*A+N*(N-1)*D/2
    print cookie