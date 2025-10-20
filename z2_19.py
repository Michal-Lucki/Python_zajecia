L=[31,4,696,8,44]
#listy=niezmienne, wiec tworze nową
nowe_L=[]

#metodą zfill wypełniam zerami to tzech cyfr każdą liczbę
#jednocześnie dodając je po kolei do nowej listy
for liczba in L:
    nowe_L.append(str(liczba).zfill(3))

print(nowe_L)
