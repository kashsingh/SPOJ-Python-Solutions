"""Solution is based on the condition derived from the formula on the link: http://www.jstor.org/stable/2691523"""
from math import sqrt
t=input()
for i in range(t):
    a,b,x,y=map(int,raw_input().split())
    if (a>b):    #make a smaller
        temp=a
        a=b
        b=temp

    if(x>y):    #make x smaller
        temp=x
        x=y
        y=temp

    if(a>x and b>y):
        print "Escape is possible."
        continue

    a,b,x,y= float(a),float(b),float(x),float(y)		
    val=abs(x**2 + y**2 - b**2)    #To make sure val is not negetive otherwise sqrt will throw an error.
    temp = (2.0*x*y*b + (y**2 - x**2)*sqrt(val))/(x**2 + y**2)
    if((a-temp)>0.0000001):
        print "Escape is possible."
    else:
        print "Box cannot be dropped."                 
    
    