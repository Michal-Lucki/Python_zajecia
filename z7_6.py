import itertools
import random

a=itertools.cycle(range(0, 2))
b=iter(lambda: random.choice(["N", "E", "W", "S"]), 0) #wg instrukcji z zestawu 7.
c=itertools.cycle(range(0,7))

#funkcja testujaca iteratry przez 10 iteracji
def TestIterator():

	test_a=""
	test_b=""
	test_c=""

	for i in range(10):
		test_a+=str(next(a))
		test_b+=str(next(b))
		test_c+=str(next(c))

	print(test_a+" "+test_b+" "+test_c)

TestIterator()