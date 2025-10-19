line="Przykladowe zdanko do testu"

#definiuje obiekt laczna_dlugosc
laczna_dlugosc=0

#rozdzielam wyrazy line'a do listy
wyrazy=line.split()

#petlą licze długości wyrazow z listy wyrazów line'a
for wyraz in wyrazy:
    laczna_dlugosc+=len(wyraz)

print(laczna_dlugosc)

