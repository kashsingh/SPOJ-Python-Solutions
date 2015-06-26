"""Although it seems to be a difficult task to perform but rather it has a very stupid solution once you figure it out 
   that the person who ever starts the game will win.
   As problem suggests the player will pick a wooden stick and remove it he will also remove other 
   wooden sticks which are multiple of it divisor. So if he picks up and wooden stick say 6( can be anyone, n) the 
   divisors are 1,2,3,6 so 1 is divisor of all number hence he will remove all the wooden sticks and wins the game 
   and answer for this problem is the player who play first will win the game."""
   
t=input()
for i in range(t):
    N,K=map(int,raw_input().split())
    if K==0:
        print "Airborne wins."
    else:
        print "Pagfloyd wins."