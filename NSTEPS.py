no=int(raw_input())
for i in range(no):
    arr=map(int,raw_input().split())
    if arr[0]==arr[1] or arr[0]-2==arr[1]:
        if arr[0]%2==0:
            print(arr[0]+arr[1])
        else:
            print(arr[0]+arr[1]-1)
    else:
        print'No Number'