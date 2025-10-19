line="Krotkie zdanie dla sprawdzenia skryptu"

#najpierw rozdzielam wyrazy z line'a
wyrazy=line.split()

#definiuje liste zawierajacą dlugosci wyrazów
rozmiary_wyrazow=[]

#petlą po wyrazach uaktualniam listę rozmiary_wyrazow
for wyraz in wyrazy:
        rozmiary_wyrazow.append(len(wyraz))

#definiuje 'najdluzszy' jako wyraz z listy 'wyrazy' o indeksie
#takim samym jak indeks najwiekszej liczby w liscie dlugosci
najdluzszy=wyrazy[rozmiary_wyrazow.index(max(rozmiary_wyrazow))]

print(najdluzszy, len(najdluzszy))


