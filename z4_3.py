#definiuje funkcje factorial
def factorial(n):
	wartosc=0
	#sytuacja wyjatkowa dla zera
	if int(n)==0:
		wartosc=1
	#petla iteracyjna dla n>0
	elif int(n)>0:
		wartosc=1
		for x in range(1,int(n)+1):
			wartosc=wartosc*x
	
	#return wraz z tekstem
	return "Silnia z "+str(n)+" wynosi: "+str(wartosc)

print(factorial(0))
print(factorial(3))
print(factorial(10))