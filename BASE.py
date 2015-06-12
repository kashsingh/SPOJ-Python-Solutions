def str_base(number, base):
   (d,m) = divmod(number,len(base))
   if d > 0:
      return str_base(d,base)+base[m]
   return base[m]
alpha="0123456789ABCDEF"

def main():    
    while True:
        try:
            case=raw_input().split()
            currentBase=int(case[1])
            convertBase=int(case[2])
            noIn10=int(case[0],currentBase)
            
            
            '''if dict1[convertBase]<noIn10:
                print "ERROR".rjust(7)
                continue'''
                
            if noIn10==0:
                print '0'.rjust(7)
                continue
                
            strNo=str_base(noIn10,alpha[:convertBase])
            lenOfStr=len(strNo)
            if lenOfStr>7:
                print "ERROR".rjust(7)
            else:
                print strNo.rjust(7)
        except:
            break
        
#LIMIT Base2:127, Base3: 2186 Base4: 16383 Base5: 78124  Base6: 279935 Base7: 823542 Base8: 2097151 Base9: 4782968 Base10:9999999
    
main()