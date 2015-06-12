# -*- coding: utf-8 -*-
'''To solve the problem 2 primary condition that should be met are:
    1. No should not be of the form 4k+3 as for sum of square of two nos will always be of form 4k or 4k+1
    2. All the prime factors of form 4k+3 should have even power from the Fermat thorem.
   Steps involved in solving the problem are:
    1. Sieve a list of prime nos. upto 1000001 as in problem. Function used here has a runtime of 0.053 s to sieve the list.
    2. Check if all the prime factors has even powers.
    3. Check if the no is not of form 4k+3'''

def sieve(n):
    """Return a list of the primes below n."""
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n ** .5) + 1) | 1    # ensure it's odd
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::2*p] = [False] * ((n - p*p - 1) // (2*p) + 1)
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result

primes=sieve(10**6+1)            #List of all the prime upto 10**6
        
def main():
    noOfCase=input()
    for i in range(noOfCase):
        N=int(raw_input())
        is_multiple= True
        i = 0
        while(primes[i]*primes[i] <= N):
	   count = 0;
	   while (N % primes[i] == 0):
	       count+=1;
	       N/= primes[i];
       	   if (primes[i]%4 == 3 and count%2 == 1):
               is_multiple = False;
               break;
       	   i+=1
		
	if (N%4 == 3):
	   is_multiple = False
	if(is_multiple):
	   print "Yes"
	else:
	   print "No"
                

main()