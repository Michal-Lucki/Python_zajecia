L=[31,4,1,59]

#definiuje separator jako pusty string
separator=""

#kleje stringi utworzone z elementów listy metoda str() 
string=separator.join(str(liczba) for liczba in L)

print(L, string)
