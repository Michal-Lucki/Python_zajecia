#ciagla petla
while True:

	#input pobierany od uzytokwnika, a wartosc kontrolna kasowana

	x=input("Podaj liczbe: ")
	wartosc_kontrolna=0

	#input zawsze jest stringiem, wiec sprawdzam znaki
	#czy kazda jest cyfra (lub kropką), porownując liczbe 
	#cyfr w stringu do dlugosci calego stringu

	for znak in x:
		if znak.isdigit() or znak==".":
			wartosc_kontrolna+=1
	
	#tylko jesli wszystkie znaki to cyfry i kropki
	if wartosc_kontrolna==len(x):
		print(float(x), float(x)**3)

	#warunek dla zatrzymania programu
	elif x=="stop":
		break
	#ani liczba, ani stop, wtedy wywalam bląd
	else:
		print("Błąd, podaj liczbe!")



	#print(float(x), float(x)**3)

	
