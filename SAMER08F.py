'''The problem is not specified for python, I didn't noticed that yet made a solution for it in python. It C++ solution is also available here.'''
def sumOfSq(n):
    if n==1:
        return 1
    else:
        return n**2+sumOfSq(n-1)

while True:
    no=input()
    if no==0:
        break
    else:
        print sumOfSq(no)