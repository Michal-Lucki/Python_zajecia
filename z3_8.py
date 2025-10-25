#definiuje sekwencje oraz puste listy
#do uzupelnienia
L1=[3,1,2,4,7,7,7]
L2=[2,0,5,4,1,6,4,3]
L_wspolne=[]
L_laczne=[]


for x in L1:

	#jesli nie ma jeszcze takiego iksa, to dodaje do lacznej
	if L_laczne.count(x)==0:
			L_laczne.append(x)

	for y in L2:
		
		#jesli nie ma takiego igreka, to dodaje do lacznej
		if L_laczne.count(y)==0:
			L_laczne.append(y)

		#jesli są elementem wspólnym, a nie ma go jeszcze
		#na liście wspolnych, to dodaje do wspólnych
		if x==y and L_wspolne.count(x)==0:
			L_wspolne.append(x)


#DOKONCZYĆ JUTRO
print(L_wspolne)
print(L_laczne)
