from points import Point #moduł points z mojego pliku points.py
from math import sqrt #do wzoru Herona
import unittest

class Triangle:

	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.pt1=Point(x1, y1)
		self.pt2=Point(x2, y2)
		self.pt3=Point(x3, y3)

		#ten zbior krotek przyda mi sie przy funkcji __eq__
		#krotki zachowują relacje miedzy x oraz y, a zbiory ułatwiaja porownanie kombinacji
		#miedzy trojkątami, bo zbiory nie uwzgledniaja kolejności
		self.pt_set={(self.pt1.x, self.pt1.y), (self.pt2.x, self.pt2.y), (self.pt3.x, self.pt3.y)}

	def __str__(self):
		return "[({}, {}), ({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

	def __repr__(self):
		return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)		

	def __eq__(self, other):

		#w zbiorach sa punkty w postaci krotek. tylko jesli zbiory sa
		#nawzajemną kombinacją to zwracam true

		#rozwazalem też iteracje po listach wspolrzednych, ale uwazam
		#że to rozwiazanie jest bardziej optymalne
		if self.pt_set==other.pt_set:
			return True
		else: return False

	def __ne__(self, other):

		return not Triangle.__eq__(self, other)

	def center(self):
		return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3, (self.pt1.y+self.pt2.y+self.pt3.y)/3)

	def area(self):
		#z wzoru Herona na pole z dlugosci boków (tu wektorów):
		#P=sqrt(p*(p-a)*(p-b)*(p-c)), gdzie:
		#a,b,c - dlugosci bokow
		#p - polowa obwodu trójkata
		
		#bok a miedzy pt1 a pt2, bok b miedzy pt2 a pt3, bok c miedzy pt3 a pt1

		#wazne zeby wekotry były rozpatrywane nie od poczatku ukladu wspolrzednych
		#dlatego biore moduł z roznicy współrzednych (chociaz pewnie jest bardziej
		#optymalny sposób, ale tylko na to wpadłem)

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

		#po modyfikacji kazdej ze wspolrzednych kazdego z wierzcholkow
		#zwracam nowy zestaw (czyli nowy trojkąt)

		return self


class TestTriangles(unittest.TestCase):

	def test_init(self):

		troj1=Triangle(3,2,8,1,7,5)
		self.assertEqual(troj1.pt2, Point(8,1))
		self.assertTrue(troj1.pt1.y==Point(3,2).y)

	def test_str(self):

		self.assertEqual(Triangle.__str__(Triangle(0,0,1,1,2,2)), "[(0, 0), (1, 1), (2, 2)]")

	def test_repr(self):

		self.assertEqual(Triangle.__repr__(Triangle(-3,1,0,0,4,2)), "Triangle(-3, 1, 0, 0, 4, 2)")

	def test_eq(self):
		
		self.assertTrue(Triangle.__eq__(Triangle(1,2,3,4,5,6), Triangle(5,6,1,2,3,4)))
		self.assertTrue(Triangle.__eq__(Triangle(0,1,0,0,1,0), Triangle(0,0,1,0,0,1)))

	def test_ne(self):
		
		self.assertTrue(Triangle.__ne__(Triangle(1,2,3,4,5,6), Triangle(6,5,4,3,2,1)))

	def test_center(self):

		self.assertEqual(Triangle.center(Triangle(2,0,0,2,0,0)), Point(2/3, 2/3))
		#przemiennosc punktow
		self.assertTrue(Triangle.center(Triangle(1,2,3,4,5,6))==Triangle.center(Triangle(3,4,5,6,1,2)))

	def test_area(self):

		#almostequal bo floaty :)
		self.assertAlmostEqual(Triangle.area(Triangle(3,0,0,5,0,0)), (3*5)/2)
		#przemiennosc punktow
		self.assertAlmostEqual(Triangle.area(Triangle(3,0,0,5,0,0)), Triangle.area(Triangle(0,0,3,0,0,5)))
		#gdy punkty sa w jednej linii, to nie da sie stworzyc trojkata (bedzie to odcinek..)
		#pole zatem bedzie rrowne 0
		self.assertTrue(Triangle.area(Triangle(1,1,2,2,3,3))==0)

	def test_move(self):
		
		self.assertTrue(Point.__eq__(Triangle.move(Triangle(1,7,4,5,8,0), 2, -1).pt1, Point(3,6)))
		troj1=Triangle(7,3,2,1,0,0)
		#przesyniecie trojkąta o 0,0 nie zmienia go, wiec powinien byc
		#równy z oryginałem (po prostu sie nie rusza)
		self.assertTrue(Triangle.__eq__(Triangle.move(troj1, 0, 0), troj1))

if __name__=='__main__':
	unittest.main()