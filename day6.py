nums=[]
with open('6.txt') as f:
    for l in f:
    	nums.append(l)
op=nums[len(nums)-1].strip().split()
aop=len(op)-1
if op[aop]=='+':
	p=0
else:
	p=1
t=0
for e in range(len(nums[0])-2,-1,-1):
	inter=""		
	for n in range(0,len(nums)-1):
		inter=inter+(nums[n][e])
	if inter.replace(" ","")=="":
		t=t+p
		aop=aop-1
		if op[aop]=='+':
			p=0
		else:
			p=1
	else:
		if op[aop]=='+':
			p=p+int(inter)
		else:
			p=p*int(inter)
t=t+p
print(t)
	
    	

