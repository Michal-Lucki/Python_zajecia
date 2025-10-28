#README
#aby wyjsc z programu wpisz "stop"
#program nie wie jak sie zachwac dla liczb zapisanych niepoprawnie

def roman2int(roman):

	wartosc=0
	odejmuj_C=False
	odejmuj_X=False
	odejmuj_I=False

	#petla po znakach w stringu
	for x in roman:
		if x=="M":
			wartosc+=1000
		if x=="D":
			wartosc+=500
		#wewnatrz są warunki, ponieważ "C" może byc odejmowalne
		if x=="C":
			for y in range(roman.index(x),len(roman)):
				if roman[y]=="D":
					odejmuj_C=True
			if odejmuj_C==True:
				wartosc-=100
			else:
				wartosc+=100
		if x=="L":
			wartosc+=50
		#wewnatrz są warunki, ponieważ "X" może byc odejmowalne
		if x=="X":
			for y in range(roman.index(x),len(roman)):
				if roman[y]=="L":
					odejmuj_X=True
			if odejmuj_X==True:
				wartosc-=10
			else:
				wartosc+=10
		if x=="V":
			wartosc+=5
		#wewnatrz są warunki, ponieważ "I" może byc odejmowalne
		if x=="I":
			for y in range(roman.index(x),len(roman)):
				if roman[y]=="X" or roman[y]=="V":
					odejmuj_I=True
			if odejmuj_I==True:
				wartosc-=1
			else:
				wartosc+=1



	return wartosc


while True:

	#biore input od uzytkownika
	liczba=input("Podaj cyfrę rzymską: ")

	#warunek schodzacy z petli
	if liczba=="stop":
		break

	#konwersja 
	print(roman2int(liczba))


