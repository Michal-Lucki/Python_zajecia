line="uzgodnione nieoczywistosci tancowaly postkomunistycznie"

#dziele line na liste wyrazow
wyrazy=line.split()

#tworze nowąliste przez alfabetyczne sortowanie
alfabetycznie=sorted(wyrazy)

#tworze nowąl iste przez sortowanie po kluczu dlugosci wyrazu
dlugosciowo=sorted(wyrazy, key=len)

print(alfabetycznie)
print(dlugosciowo)
