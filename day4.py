def veins(matriu, i, j):
    files = len(matriu)
    cols = len(matriu[0])
    veïns = []
    direccions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for df, dc in direccions:
        ni, nj = i + df, j + dc

        # Comprovar que està dins dels límits
        if 0 <= ni < files and 0 <= nj < cols:
            veïns.append(matriu[ni][nj])

    return veïns

mat=[]
with open('4.txt') as f:
    for l in f:
    	l=l.strip()
    	mat.append(list(l))
    	
print(mat)
mogutsit=1 
it=0
tot=0
while mogutsit>0:
	mogutsit=0
	canvis=[]
	for i in range(0,len(mat)):
		for j in range(0,len(mat[0])):		
			if mat[i][j]=='@':
				linia=veins(mat,i,j)
				total=linia.count('@')			
				if total<4:
					print(i,j)
					#mat[i][j]='.'
					canvis.append([i,j])
					mogutsit=mogutsit+1
	print("en la it " , it , " s'han mogut " , mogutsit)
	tot=tot+mogutsit
	print(canvis)
	for i in canvis:
		mat[i[0]][i[1]]='.'
	it=it+1
print(tot)

