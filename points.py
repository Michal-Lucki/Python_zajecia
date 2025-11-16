import unittest
from math import sqrt #dla pierwiastkow w liczeniu dlugosci 

class Point:

	#Metody punktów jako punktów

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

	#wprowadzam funkcje mul_values, zeby ulatwic sobie testy
	#na roznych punktach/wektorach
	#UWAGA: iloczyn skalarny jest nizej, to jedynie skalowane x i y!
	def mul_values(self, a):
		return Point(self.x*float(a), self.y*float(a))

	#Metody punktów jako wektorów (para liczb - wspolrzedne wektorów)

	def __add__(self, other):
		return Point(self.x+other.x, self.y+other.y)

	def __sub__(self, other):
		return Point(self.x-other.x, self.y-other.y)

	def __mul__(self, other):
		#iloczyn skkalarny [x1, y1]·[x2, y2]= x1x2+y1y2
		return self.x*other.x+self.y*other.y

	def cross(self, other):
		return self.x*other.y-self.y*other.x

	def length(self):
		#z pitagorasa
		return sqrt(self.x**2+self.y**2)

	def __hash__(self):
		return (hash(self.x), hash(self.y))

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
		#floaty takie same, mimo zer po przecinku
		self.assertTrue(Point.__eq__(pkt1, pkt2))
		#zmiana wspolrzednej x-owej niszczy rownosc
		pkt2.x+=0.1
		self.assertFalse(Point.__eq__(pkt1, pkt2))

	def test_ne(self):

		pkt1=Point(7.1, -2.99)
		pkt2=Point(7.1, -3)
		#analogicznie
		self.assertTrue(Point.__ne__(pkt1, pkt2))
		pkt2.y+=0.01
		self.assertFalse(Point.__ne__(pkt1, pkt2))

	def test_mul_values(self):

		pkt1=Point(3, 1)
		self.assertEqual(pkt1.mul_values(6), Point(18, 6))
		#string nie da sie przeksztalcic tutaj we floata do mnozenia
		self.assertRaises(ValueError, pkt1.mul_values, "x")

	def test_add(self):

		pkt1=Point(1, 4.1)
		pkt2=Point(-1, -4.1)

		self.assertTrue(Point(0,0)==Point.__add__(pkt1, pkt2))
		#poniewaz uzywam floatow, to wynikiem jest 36.89999999,
		#dlatego uzywam AssertAlmostEqual do trzech miejsc
		self.assertAlmostEqual(Point.__add__(pkt1.mul_values(2), pkt2.mul_values(-7)).y, 36.9, places=3)

	def test_sub(self):

		pkt1=Point(0.01, 4)
		pkt2=Point(7, 10.99)

		self.assertFalse(Point.__sub__(pkt1, pkt2)==Point.__sub__(pkt2, pkt1))
		#nie mozna odjac inta od punktu
		self.assertRaises(AttributeError, Point.__sub__, pkt1, 5)

	def test_mul(self):
		
		pkt1=Point(2, 0)
		pkt2=Point(0, 7.1)
		pkt3=Point(1, -7.1)
		self.assertEqual(Point.__mul__(pkt1, pkt2), 0)
		self.assertEqual(Point.__mul__(pkt2, pkt3), -50.41)
		#analogicznie: nie mozna zrobić iloczynu sklaranego ze skalara (inta) i wektora
		self.assertRaises(AttributeError, Point.__mul__, 3, pkt1)

	def test_cross(self):

		pkt1=Point(2, 0)
		pkt2=Point(0, 7.1)
		pkt3=Point(10,10)
		self.assertEqual(Point.cross(pkt1, pkt2), 14.2)
		#dla danych wektorow (niezerowych) iloczyn wektorowy jest nieprzemienny
		self.assertFalse(Point.cross(pkt1, pkt2)==Point.cross(pkt2, pkt1))


	def test_length(self):

		self.assertEqual(Point.length(Point(1,1)), sqrt(2))
		#przemiennosc wspolrzednych
		self.assertEqual(Point.length(Point(4.2, 6.9)), Point.length(Point(6.9, 4.2)))

	def test_hash(self):

		self.assertEqual(Point.__hash__(Point(3, -2)), (hash(3), hash(-2)))


if __name__=='__main__':
	unittest.main()
