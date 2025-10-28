#definiuje docelowego stringa
prostokat=""

while True:

	#definiuje i zbieram z inputu wymiary prostokata n ✕ m
	n=input("podaj liczbe kolumn: ")
	m=input("podaj liczbe wierszy: ")

	#nadrzedną petlaą po liczbie kolumn buduje każdy z wierszy 
	for y in range(0, int(m)+1):
		
		for x in range(0, int(n)):
			prostokat+="+---"

		prostokat+="+\n"

		#warunkowo o jeden mniej wiersz pionowych pasków, aby
		#dolny border siatki byl zamkniety
		if y<=int(m)-1:
			for x in range(0, int(n)):
				prostokat+="|   "
			prostokat+="|\n"

	#tutaj wychodze z petli, ale moglbym tez nie dawac
	#break'a i pozwolic uzytkownikowi w petli wczytywac
	#prostokaty. nie zaimplementowalem jednak furtki dla
	#wyjscia z petli, wiec po prostu wychodze break'iem
	break	

print(prostokat)
		