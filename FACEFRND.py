def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return False
        m = int((min + max)/2)
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return True

def mergeSort(L):
    if len(L)<2:
        return L
    else:
        middle=int(len(L)/2)
        left=mergeSort(L[:middle])
        right=mergeSort(L[middle:])
    return merge(left,right)
    
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])   
            j+=1
    while(i<len(left)):
        result.append(left[i])
        i+=1
    while(j<len(right)):
        result.append(right[j])
        j+=1
    return result
    
def main():
    noOfFrnds=int(raw_input())
    bobFrnd=[]
    frndCheck=[]
    for i in range(noOfFrnds):
       tempList= []
       tempList=map(int,raw_input().split())
       bobFrnd.append(tempList[0])
       for j in tempList[2:]:
           frndCheck.append(j)
    frndCheck=list(set(frndCheck))
    frndCheck= mergeSort(frndCheck)
    sum1=len(frndCheck)
    for j in bobFrnd:
        if (binary_search(frndCheck,j))==True:
            sum1-=1
            
    print(sum1)
    
    
main()
    