L=[[2,1,1,1],(4,0),(1,6),[3,4],[-25,6,7]]
L_suma=[]

for seq in L:

	#zeruje sume, zeby dla kazdej sekwencji zaczynać od zera
	suma=0

	for x in seq:
		suma+=x

	#po zsumowaniu wartosci w sekwencji, załaczam ją do listy sumy
	#i petlą ide do nastepnej seq w liscie L
	L_suma.append(suma)

print(L_suma)