while True:
    noOfCase=int(raw_input())
    if noOfCase<0:
        break
    else:
        series=[]
        for i in range(noOfCase):
            series.append(int(raw_input()))
        sum1=0
        for i in series:
            sum1+=i
        if sum1%noOfCase==0:
            avg=sum1/noOfCase
            moves=0
            for i in series:
                if (avg-i)<0:
                    moves+=i-avg
            print(moves)
        else:
            print(-1)