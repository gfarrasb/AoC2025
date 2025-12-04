i=50
t=0
with open('1.txt') as f:
    for l in f:
    	n=int(l[1::]) 
    	if n>100:
    		t=t+(n//100)
    		n=n%100
    	if l[0]=="R":
    		if i+n>100 and i!=100 and i!=0:
    			t=t+1
    			print("R+1")
    		i=(i+n)%100
    	elif l[0]=="L":
    		if i-n<0 and i!=100 and i!=0:
    			t=t+1
    			print("L+1")
    		i=(i-n)%100
    	if i==0:
    		t=t+1
    		print("i es 0")
    	print(l)
print(t)









#	if l[0]=="R":
#		
#	elif l[0]=="L":
#		i=(i-n)%100
 #       if i==0:
  #      	t=t+1
        

