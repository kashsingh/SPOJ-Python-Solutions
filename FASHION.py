__author__ = 'Alxetraz'
def getIt(noCases):
    allCases=[]
    allCases_men=[]
    allCases_women=[]
    raw_input()
    allCases_men.append(map(int,raw_input().split()))
    allCases_women.append(map(int,raw_input().split()))
    allCases=allCases_men+allCases_women
    return allCases

def calculate(Tcases):
    sum=0
    for i in range(len(Tcases[0])):
        sum+=Tcases[0][i]*Tcases[1][i]
    return sum
    
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
    result=[]
    noCases=int(raw_input())
    for i in range(noCases):
        Tcases=getIt(noCases)
        newCases1=mergeSort(Tcases[0])
        newCases2=mergeSort(Tcases[1])
        allCases=[]
        allCases.append(newCases1)
        allCases.append(newCases2)
        result.append(calculate(allCases))
    for i in result:
        print(i)

main()