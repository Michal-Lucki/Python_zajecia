#zmodyfikowałem skrypt points.py (nowy skrypt points_n.py),
#dodając dwie nowe funkcje dla klasy Points: line_eqt i belong2line
#korzystając z nich zabezpieczyłem funkcje __init__ w klasie Triangle
#przed punktami współliniowymi

from points_n import Point 
from math import sqrt
import unittest

class Triangle():

	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.pt1=Point(x1, y1)
		self.pt2=Point(x2, y2)
		self.pt3=Point(x3, y3)

		#warunek: czy pt1 nalezy do prostej przechodzacej przez pt2 i pt3?
		#innymi słowy: czy wszystkie trzy punkty leza na tej samej prostej?

		#najpierw sprawdzam czy to prosta pionowa x=b
		if isinstance(Point.line_eqt(self.pt2, self.pt3), int):
			if self.pt1.x==Point.line_eqt(self.pt2, self.pt3):
				raise ValueError("Punkty na jednej linii!")

		#jesli prosta to tuple (a wiec liniowa nie pionowa) to badam
		#czy pt1 nalezy do prostej z rownania pt2/pt3
		elif isinstance(Point.line_eqt(self.pt2, self.pt3), tuple):
			if Point.belong2line(self.pt1, Point.line_eqt(self.pt2, self.pt3)[0], Point.line_eqt(self.pt2, self.pt3)[1]):
				raise ValueError("Punkty na jednej linii!")

		

	def __str__(self):
		return "[({}, {}), ({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

	def __repr__(self):
		return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)		

	def __eq__(self, other):
		#zgodnie z Pana wskazówką, usunałem atrybut self.pt_set i tworze zbiór krotek (punktow)
		#dopiero w ramach funkcji __eq__
		if {(self.pt1.x, self.pt1.y), (self.pt2.x, self.pt2.y), (self.pt3.x, self.pt3.y)}=={(other.pt1.x, other.pt1.y), (other.pt2.x, other.pt2.y), (other.pt3.x, other.pt3.y)}:
			return True
		else: return False

	def __ne__(self, other):

		return not Triangle.__eq__(self, other)

	def center(self):
		return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3, (self.pt1.y+self.pt2.y+self.pt3.y)/3)

	def area(self):
		a=Point.length(Point(abs(self.pt1.x-self.pt2.x), abs(self.pt1.y-self.pt2.y)))
		b=Point.length(Point(abs(self.pt2.x-self.pt3.x), abs(self.pt2.y-self.pt3.y)))
		c=Point.length(Point(abs(self.pt3.x-self.pt1.x), abs(self.pt3.y-self.pt1.y)))

		p = (a+b+c)/2
		return sqrt(p*(p-a)*(p-b)*(p-c))

	def move(self, x, y):
		self.pt1.x+=x
		self.pt2.x+=x
		self.pt3.x+=x

		self.pt1.y+=y
		self.pt2.y+=y
		self.pt3.y+=y

		return self

	def make4(self):

		#potrzebuje trzech nowych punktów - centrów boków a (pt1:pt2), b (pt2:pt3), c (pt3:pt1)
		#punkt srodkowy punktow (a, b) i (c, d) to punkt ((a+b)/2, (c+d)/2)
		#co więdej, pole każdego z czeterch trojkątów powinien mieć równe pole (dokładnie 1/4 oryginalnego) - to ważne w testach

		self.a_cen=Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)
		self.b_cen=Point((self.pt2.x+self.pt3.x)/2, (self.pt2.y+self.pt3.y)/2)
		self.c_cen=Point((self.pt1.x+self.pt3.x)/2, (self.pt1.y+self.pt3.y)/2)

		return (Triangle(self.pt1.x, self.pt1.y, self.a_cen.x, self.a_cen.y, self.c_cen.x, self.c_cen.y),
				Triangle(self.pt2.x, self.pt2.y, self.a_cen.x, self.a_cen.y, self.b_cen.x, self.b_cen.y),
				Triangle(self.pt3.x, self.pt3.y, self.b_cen.x, self.b_cen.y, self.c_cen.x, self.c_cen.y),
				Triangle(self.a_cen.x, self.a_cen.y, self.b_cen.x, self.b_cen.y, self.c_cen.x, self.c_cen.y))

class TestTriangles(unittest.TestCase):

	def test_init(self):

		troj1=Triangle(3,2,8,1,7,5)
		self.assertEqual(troj1.pt2, Point(8,1))
		self.assertTrue(troj1.pt1.y==Point(3,2).y)

		#nowy test liniowosci punktów
		
		#self.assertRaises(ValueError, Triangle(1,1,2,2,3,3)) nie działa, wiec znalazłem w internecie
		#sposob testowania z użyciem with

		with self.assertRaises(ValueError):
			#wszystkie punkty na prostej y=x
			Triangle(1,1,2,2,3,3)

		with self.assertRaises(ValueError):
			#wszystkie punkty na prostej x=7
			Triangle(7,3,7,9,7,11)


	def test_str(self):

		self.assertEqual(str(Triangle(0,3,1,1,4,2)), "[(0, 3), (1, 1), (4, 2)]")

	def test_repr(self):

		self.assertEqual(repr(Triangle(-3,1,0,0,4,2)), "Triangle(-3, 1, 0, 0, 4, 2)")

	def test_eq(self):
		
		self.assertTrue(Triangle(1,4,2,4,5,6)==Triangle(5,6,2,4,1,4))
		#tu tylko dwa punkty są na prostej x=0 i tylko dwa na prostej y=0, wiec
		#nie ma wyjatku ValueError!
		self.assertTrue(Triangle(0,1,0,0,1,0)==Triangle(0,0,1,0,0,1))

	def test_ne(self):
		
		self.assertTrue(Triangle(0,8,1,7,3,9)!=Triangle(0,8,1,7,9,3))

	def test_center(self):

		self.assertEqual(Triangle(2,0,0,2,0,0).center(), Point(2/3, 2/3))
		self.assertTrue(Triangle(1,2,7,4,5,6).center()==Triangle(7,4,5,6,1,2).center())

	def test_area(self):

		self.assertAlmostEqual(Triangle(3,0,0,5,0,0).area(), (3*5)/2)
		self.assertAlmostEqual(Triangle(3,0,0,5,0,0).area(), Triangle(0,0,3,0,0,5).area())

	def test_move(self):
		
		self.assertTrue(Point.__eq__(Triangle(1,7,4,5,8,0).move(2, -1).pt1, Point(3,6)))
		troj1=Triangle(7,3,2,1,0,0)
		self.assertTrue(Triangle.__eq__(troj1.move(0,0), troj1))

	def test_make4(self):

		#pola rowne dla wszystkich trojkatow
		trojkat=Triangle(1,7,5,4,3,9)
		trojkaty=trojkat.make4()
		for x in range(3):
			self.assertAlmostEqual(trojkaty[x].area(), trojkaty[x+1].area())

		#centrum trojkata z punktow srodkowych musi byc takie samo, jak centrum
		#oryginalnego trójkata
		self.assertEqual(trojkat.center(), trojkaty[3].center())
		

if __name__=='__main__':
	unittest.main()