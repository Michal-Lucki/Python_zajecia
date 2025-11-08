import unittest
from functools import reduce #aby korzystać z reduce'a w hornerze

#uwaga: nie udalo mi sie napisać żadnego "rozsądnego"
#pomysłu dla funkcji combine_poly

def add_poly(poly1, poly2):
	#nowa lista bedaca wielomianem (sumą)
	poly_suma=[]

	if len(poly1)>len(poly2):
		for x in range(len(poly1)):
			if x<len(poly2):
				poly_suma.append(poly1[x]+poly2[x])
			else:
				poly_suma.append(poly1[x])
	else:
		for x in range(len(poly2)):
			if x<len(poly1):
				poly_suma.append(poly1[x]+poly2[x])
			else:
				poly_suma.append(poly2[x])

	return(poly_suma)

def sub_poly(poly1, poly2):
	#nowa lista bedącą wielomianem (różniccą)
	poly_roznica=[]

	if len(poly1)>len(poly2):
		for x in range(len(poly1)):
			if x<len(poly2):
				poly_roznica.append(poly1[x]-poly2[x])
			else:
				poly_roznica.append(poly1[x])
	else:
		for x in range(len(poly2)):
			if x<len(poly1):
				poly_roznica.append(poly1[x]-poly2[x])
			else:
				poly_roznica.append(-poly2[x])

	return poly_roznica

def mul_poly(poly1, poly2):

	poly_mnozenie=[]

	for a in range(len(poly1)+len(poly2)-1):
		poly_mnozenie.append(0)

	for x in range(len(poly1)):
		for y in range(len(poly2)):
			poly_mnozenie[x+y]+=poly1[x]*poly2[y]

	return poly_mnozenie

def is_zero(poly):

	if poly.count(0)!=len(poly):
		return False
	else:
		return True

def eq_poly(poly1, poly2):

	if is_zero(sub_poly(poly1,poly2)):
		return True
	else:
		return False

def eval_poly(poly1, x0):
	#korzystam z algorytmu Hornera w postaci
	#z zestawu 4.

	return reduce(lambda a,b: a*x0+b, reversed(poly1))

def pow_poly(poly, n):

	#ustawiam wielomian jako startowy
	poly_potega=poly

	if n==1:
		return poly_potega

	elif n>1:
		for x in range(n-1):
			poly_potega=mul_poly(poly, poly_potega)
		return poly_potega

def diff_poly(poly):
	
	poly_pochodna=[]

	for x in range(1, len(poly)):
		poly_pochodna.append(poly[x]*x)

	return poly_pochodna


class TestPolynomials(unittest.TestCase):

	def test_add_poly(self):
		self.assertEqual(add_poly([1,2], [4,0,0,1]), [5,2,0,1])

	def test_sub_poly(self):
		self.assertEqual(sub_poly([5,-4,8], [2,0,-3]), [3,-4,11])

	def test_mul_poly(self):
		self.assertEqual(mul_poly([2,4,0,0,0,1], [-7,3]), [-14,-22,12,0,0,-7,3])

	def test_is_zero(self):
		self.assertFalse(is_zero([0,0,0,1,0]))

	def test_eq_poly(self):
		self.assertTrue(eq_poly([1,2,3,0,0,0], [1,2,3]))

	def test_eval_poly(self):
		self.assertEqual(eval_poly([3,2,1], 2), 11)

	def test_pow_poly(self):
		self.assertEqual(pow_poly([1,2,1], 3), [1,6,15,20,15,6,1])

	def test_diff_poly(self):
		self.assertEqual(diff_poly([-3,7,0,4]), [7,0,12])

	def tearDown(self):
		pass

if __name__=='__main__':
	unittest.main()