def getIt():
    allCases=[]
    while True:
        inputCase=raw_input()
        if inputCase=='BYE':
            return allCases
        else:
            allCases.append(inputCase.split('+'))
            allCases[-1][1]=allCases[-1][1][:-1]

def convert(value):
    dictVal={'063':'0','010':'1','093':'2','079':'3','106':'4','103':'5','119':'6','011':'7','127':'8','107':'9'}
    i=0
    out=''
    try:
        while i<len(value):
            out+=dictVal[value[i:i+3]]
            i+=3
    except KeyError:
        return None
    return int(out)
        

def reverseConvert(result):
    dictRevVal={'0':'063','1':'010','2':'093','3':'079','4':'106','5':'103','6':'119','7':'011','8':'127','9':'107'}
    out=''
    try:
        for i in str(result):
            out+=dictRevVal[i]
    except KeyError:
        return None
    return out
    
def main():
    Tcases=getIt()
    if len(Tcases)>0:
        for case in Tcases:
            a=case[0]
            b=case[1]
            try:
                result=convert(a)+convert(b)
                print(case[0]+'+'+case[1]+'='+reverseConvert(result))
            except TypeError:
                continue
        
main()