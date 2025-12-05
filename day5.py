rangs=[]
with open('5b.txt') as f:
    for l in f:
    	l=l.strip()
    	a,b=l.split("-")
    	a=int(a)
    	b=int(b)  
    	rangs.append([a,b])  	
print(rangs)
print("init")
l=len(rangs)
it=0
while True:
	for i in range(0,l):
		for j in range(0,l):		
			if i==j:
				break
			#print("comparem " , rangs[i] , " amb " , rangs[j] )
			if rangs[i][0] >= rangs[j][0] and rangs[i][1] <= rangs[j][1]:
			#	print("cas a")
				rangs[i][0],rangs[i][1]=0,0
			elif rangs[i][0]<=rangs[j][0] and rangs[i][1]>=rangs[j][1]:
				rangs[j][0],rangs[j][1]=0,0
			elif rangs[i][0]>=rangs[j][0] and rangs[i][0]<=rangs[j][1] and rangs[i][1]>=rangs[j][1]:
			#	print("cas c")
				rangs[j][1]=rangs[i][1]
			elif rangs[i][0]<=rangs[i][0] and rangs[i][1]<=rangs[j][1] and rangs[i][1]>=rangs[j][0]:
			#	print("cas d")
				rangs[j][0]=rangs[i][0]
	print(it , " " , rangs)
	tot=0
	for i in rangs:
		if i[1]!=0 and i[0]!=0:
			tot=tot+i[1]-i[0]+1
	print(it, tot)
	it=it+1
		
	
	
