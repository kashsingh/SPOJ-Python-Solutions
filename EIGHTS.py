noOfCases=int(raw_input())
for i in range(noOfCases):
	n=int(raw_input())
	if (n-1)%4==0:
		str1="192"
	elif (n-1)%4==1:
		str1="442"
	elif (n-1)%4==2:
		str1="692"
	else :
		str1="942"
	if n<=4:
		print str1
	else:
		str2=str((n-1)/4)
		print str2+str1