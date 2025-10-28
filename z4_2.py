
def make_ruler(n):
	
	#definiuje string miarki 
	miarka=""
	
	#buduje "ośkę" miarki
	for x in range(0, int(n+1)):
		miarka+="|"
	miarka="....".join(miarka)+"\n"

	#na koncu dodalem jeszcze przejscie do nastepnego wierssza

	#teraz robie cyfry pod działkami ośki
	for x in range(0, int(n+1)):
		
		miarka=miarka+str(x)

		#w zaleznosci od tego ile liczba ma cyfr
		#ustalam ile dodać spacji
		spacje=""
		for y in range(0,5-len(str(x+1))):
			spacje+=" "
		miarka+=spacje
		
	return print("Miarka o dlugosci "+str(n)+":\n\n"+miarka+"\n")

def make_grid(rows, cols):
	#definiuje docelowego stringa
	prostokat=""


	#nadrzedną petlą po liczbie kolumn buduje każdy z wierszy 
	for y in range(0, int(rows)+1):
			
		for x in range(0, int(cols)):
			prostokat+="+---"

		prostokat+="+\n"

		#warunkowo o jeden mniej wiersz pionowych pasków, aby
		#dolny border siatki byl zamkniety
		if y<=int(rows)-1:
			for x in range(0, int(cols)):
				prostokat+="|   "
			prostokat+="|\n"

	return print("Prostkat o wymiarach "+str(rows)+"x"+str(cols)+":\n\n"+prostokat+"\n")

#przywoluje funkcje z przykladowymi argumentami
make_ruler(5)
make_ruler(11)
make_grid(2,3)
make_grid(5,5)
