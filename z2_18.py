duza_liczba=201237002708
liczba_zer=0

#duza liczbe zmieniam na string zeby latwo zapętlić
#po znakach. licznik liczba_zer liczy same zera

for cyfra in str(duza_liczba):
    if cyfra=="0":
        liczba_zer+=1

print(liczba_zer)

