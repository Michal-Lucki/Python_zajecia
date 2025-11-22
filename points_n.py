import unittest
from math import sqrt

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "({}, {})".format(self.x, self.y)

	def __repr__(self):
		return "Point({}, {})".format(self.x, self.y)

	def __eq__(self, other):
		return self.x==other.x and self.y==other.y

	def __ne__(self, other):
		return not Point.__eq__(self, other)

	def __add__(self, other):
		return Point(self.x+other.x, self.y+other.y)

	def __sub__(self, other):
		return Point(self.x-other.x, self.y-other.y)

	def __mul__(self, other):
		#zgodnie z Pana wskazówką rozszerzylem funkcje mul o mozliwosc mnozenia przez inta
		#zamiast osobnej funkcji mul_values
		if isinstance(other, int):
			return Point(self.x*other, self.y*other)
		elif isinstance(other, Point):
			return self.x*other.x+self.y*other.y

	def cross(self, other):
		return self.x*other.y-self.y*other.x

	def length(self):
			return sqrt(self.x**2+self.y**2)

	def __hash__(self):
		return (hash(self.x), hash(self.y))
	
	#Nowe metody.
	
	def line_eqt(self, other): 
		
		#wyznacza rownanie prostej przechodzacej przez dwa punkty
		#w postaci rownanie y=ax+b (tzn. zwraca krotke (a, b))
		
		#a=dy/dx
		try:
			a=(max(self.y, other.y)-min(self.y, other.y))/(max(self.x, other.x)-min(self.x, other.x))
			b=self.y-self.x*a
			return (a, b)
			
		except ZeroDivisionError:
			#prosta równolegla do osi OY
			b=self.x
			return b
			
	def belong2line(self, a, b):
		
		#sprawdza, czy punkt nalezy do prostej y=ax+b
		if self.y==self.x*a+b:
			return True
		else: return False 

	
class TestPoints(unittest.TestCase):

	def test_init(self):

		self.assertEqual(Point(1.41,7.0).x, 1.41)
		self.assertEqual(Point(3.01,-9).y, -9)

	def test_repr(self):

		self.assertTrue(repr(Point(3.0,-11.1))=="Point(3.0, -11.1)")
		self.assertFalse(repr(Point(1,1))==str(Point(1,1)))

	def test_eq(self):

		pkt1=Point(1.0, 4.10)
		pkt2=Point(1.000000, 4.1)

		self.assertTrue(pkt1==pkt2)

		pkt2.x+=0.1
		self.assertFalse(pkt1==pkt2)

	def test_ne(self):

		pkt1=Point(7.1, -2.99)
		pkt2=Point(7.1, -3)

		self.assertTrue(pkt1!=pkt2)
		pkt2.y+=0.01
		self.assertFalse(pkt1!=pkt2)

	def test_add(self):

		pkt1=Point(1, 4.1)
		pkt2=Point(-1, -4.1)

		self.assertTrue(Point(0,0)==pkt1+pkt2)
		self.assertAlmostEqual(Point.__add__(pkt1*2, pkt2*(-7)).y, 36.9, places=3)

	def test_sub(self):

		pkt1=Point(0.01, 4)
		pkt2=Point(7, 10.99)

		self.assertFalse(pkt1-pkt2==pkt2-pkt1)
		self.assertRaises(AttributeError, Point.__sub__, pkt1, 5)

	def test_mul(self):
		

		pkt1=Point(2, 0)
		pkt2=Point(0, 7.1)
		pkt3=Point(1, -7.1)
		self.assertEqual(pkt1*pkt2, 0)
		self.assertEqual(pkt2*pkt3, -50.41)
		#najpierw punkt, potem int
		self.assertRaises(AttributeError, Point.__mul__, 3, pkt1)

	def test_cross(self):

		pkt1=Point(2, 0)
		pkt2=Point(0, 7.1)
		pkt3=Point(10,10)
		self.assertEqual(Point.cross(pkt1, pkt2), 14.2)
		self.assertFalse(Point.cross(pkt1, pkt2)==Point.cross(pkt2, pkt1))


	def test_length(self):

		self.assertEqual(Point(1,1).length(), sqrt(2))
		self.assertEqual(Point(4.2, 6.9).length(), Point(6.9, 4.2).length())

	def test_hash(self):

		self.assertEqual(Point.__hash__(Point(3, -2)), (hash(3), hash(-2)))
	
	def test_line_eqt(self):
	
		self.assertTrue(Point.line_eqt(Point(1, 2), Point(8,6))==(4/7, 10/7))
		self.assertTrue(Point.line_eqt(Point(7, 4), Point(7, 11))==7)
	
	def test_belong2line(self):
		
		punkcik1=Point(1, 4)
		punkcik2=Point(1, 11)
		prosta=Point.line_eqt(Point(1, 4), Point(6, 9))
		
		self.assertTrue(Point.belong2line(punkcik1, prosta[0], prosta[1]))
		self.assertTrue(isinstance(Point.line_eqt(punkcik1, punkcik2), int))

if __name__=='__main__':
	unittest.main()
