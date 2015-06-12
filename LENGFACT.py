# -*- coding: utf-8 -*-
'''Dmitry Kamenetsky's formula for calculating length of factorial (log(2πn)/2+n(logn−loge))/log10]+1'''
import math
PI= math.pi
e=math.e

def lengFact(n):
    if n<3:
        print 1
    else:    
        length=math.log10(2*PI*n)/2+math.log10(n/e)*n+1
        print int(length)
    
def main():
    t=input()
    for i in range(t):
        lengFact(input())
main()
