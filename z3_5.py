#!/usr/bin/env python3
#pobieram od użytkownika żądana dlugosc linijki
dlugosc = input("Podaj dlugosc: ")
#definiuje string miarki 
miarka=""

#buduje "ośkę" miarki
for x in range(0, int(dlugosc)+1):
	miarka+="|"
miarka="....".join(miarka)+"\n"

#na koncu dodalem jeszcze przejscie do nastepnego wierssza

#teraz robie cyfry pod działkami ośki
for x in range(0, int(dlugosc)+1):
	
	miarka=miarka+str(x)

	#w zaleznosci od tego ile liczba ma cyfr
	#ustalam ile dodać spacji
	spacje=""
	for y in range(0,5-len(str(x+1))):
		spacje+=" "
	miarka+=spacje

print(miarka)