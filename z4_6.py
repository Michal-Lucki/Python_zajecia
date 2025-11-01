#definiuje sume wartosci
suma=0

def sum_seq(sequence):
	#co wazne, ustalam sume jako zmienną globalną!
	global suma
	for x in sequence:
		if isinstance(x, (list, tuple)):
			#rekurencja  dla subsekwencji
			sum_seq(x)
		else:
			suma+=x
	return suma

sekwencja=[10, (3,6), 0, [(7,1), (6, 11), (), 4]]

print(sum_seq(sekwencja))