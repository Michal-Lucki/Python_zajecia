#definiuje funkcje fibonacci
def fibonacci(n):
	#a priori definiuje dwa pierwsze wyrazy ciagu
	wyrazy=[0,1]

	#warunek dla n=1
	if int(n)==1:
		return str(n)+". wyraz ciagu fibonacciego wynosi: "+str(wyrazy[0])

	#warunek dla n>1
	elif int(n)>1:
		for x in range(1, int(n+1)):
			#dodaje dwa ostantie wyrazy
			wyrazy.append(wyrazy[x]+wyrazy[x-1])

		#dodaje opis i wynik n-tego wyraziu
	return str(n)+". wyraz ciagu fibonacciego wynosi: "+str(wyrazy[n])

print(fibonacci(1))
print(fibonacci(7))
print(fibonacci(11))
