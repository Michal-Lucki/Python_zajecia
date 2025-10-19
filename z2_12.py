line="ten atari kuleje"

#definuje obiekty 'pierwsze' i 'ostatnie', aby móc ich później użyć

pierwsze=""
ostatnie=""

#rozdzielam wyrazy z line'a

wyrazy=line.split()

#używam pętli po wyrazach w utworzonej liście, budując nowe stringi z pierwszych i ostatnich liter

for wyraz in wyrazy:
    pierwsze+=wyraz[0]
    ostatnie+=wyraz[len(wyraz)-1]

print(pierwsze, ostatnie)
 
