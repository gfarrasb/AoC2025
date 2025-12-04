t=0
with open('3.txt') as f:
    for l in f:
    	l=l.strip()
    	bat=""
    	for i in range(0,12):
    		n=max(l[0:len(l)-12+i+1])
    		pos=l.index(n)+1
    		l=l[pos::]
    		bat=bat+n
    	t=t+int(bat)
print(t)
