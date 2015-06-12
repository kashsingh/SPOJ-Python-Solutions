from datetime import datetime, timedelta

a=int(raw_input())
p = 4000000007
k= (p-3)/4
sqrt = pow(a, k+1, p)
if sqrt > p / 2:
    noOfSec= p - sqrt
else:
    noOfSec= sqrt
myDate = datetime(1970, 1, 1, 00, 00)
attackDate=myDate+timedelta(seconds=noOfSec)
print attackDate.ctime()