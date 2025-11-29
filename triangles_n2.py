from points_n import Point 
from math import sqrt

class Triangle():

	#nowa funkcja
	def from_points(points):
		if isinstance(points, tuple) or isinstance(points, list):
			coords=[]
			for point in points:
				if isinstance(point, Point):
					coords.append(point.x)
					coords.append(point.y)
				else:
					raise ValueError("Podaj punkty!")
			return Triangle(coords[0], coords[1], coords[2], coords[3], coords[4], coords[5])
		else:
			raise ValueError("Podaj krotke lub liste!")

	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.pt1=Point(x1, y1)
		self.pt2=Point(x2, y2)
		self.pt3=Point(x3, y3)
		
		#zmieniłem sprawdzanie współliniowosci punktow
		if (self.pt2-self.pt1).cross(self.pt3-self.pt1)==0:
			raise ValueError("Punkty na jednej linii!")
		

	def __str__(self):
		return "[({}, {}), ({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

	def __repr__(self):
		return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)		

	def __eq__(self, other):
		if {(self.pt1.x, self.pt1.y), (self.pt2.x, self.pt2.y), (self.pt3.x, self.pt3.y)}=={(other.pt1.x, other.pt1.y), (other.pt2.x, other.pt2.y), (other.pt3.x, other.pt3.y)}:
			return True
		else: return False

	def __ne__(self, other):

		return not Triangle.__eq__(self, other)

	@property
	def center(self):
		return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3, (self.pt1.y+self.pt2.y+self.pt3.y)/3)

	@property
	def area(self):
		a=Point.dist(self.pt1, self.pt2)
		b=Point.dist(self.pt2, self.pt3)
		c=Point.dist(self.pt3, self.pt1)

		p = (a+b+c)/2
		return sqrt(p*(p-a)*(p-b)*(p-c))

	#zmienilem sposób działania funkcji move
	def move(self, x, y):
		pt1x=self.pt1.x
		pt1y=self.pt1.y
		pt2x=self.pt2.x
		pt2y=self.pt2.y
		pt3x=self.pt3.x
		pt3y=self.pt3.y
		return Triangle(pt1x+x, pt1y+y, pt2x+x, pt2y+y, pt3x+x, pt3y+y)

	def make4(self):
		self.a_cen=Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)
		self.b_cen=Point((self.pt2.x+self.pt3.x)/2, (self.pt2.y+self.pt3.y)/2)
		self.c_cen=Point((self.pt1.x+self.pt3.x)/2, (self.pt1.y+self.pt3.y)/2)

		return (Triangle(self.pt1.x, self.pt1.y, self.a_cen.x, self.a_cen.y, self.c_cen.x, self.c_cen.y),
				Triangle(self.pt2.x, self.pt2.y, self.a_cen.x, self.a_cen.y, self.b_cen.x, self.b_cen.y),
				Triangle(self.pt3.x, self.pt3.y, self.b_cen.x, self.b_cen.y, self.c_cen.x, self.c_cen.y),
				Triangle(self.a_cen.x, self.a_cen.y, self.b_cen.x, self.b_cen.y, self.c_cen.x, self.c_cen.y))
	

	#liczby - wspolrzędne skrajne bboxa
	@property
	def top(self):
		return max(self.pt1.y, self.pt2.y, self.pt3.y)
	@property
	def bottom(self):
		return min(self.pt1.y, self.pt2.y, self.pt3.y)
	@property
	def left(self):
		return min(self.pt1.x, self.pt2.x, self.pt3.x)
	@property
	def right(self):
		return max(self.pt1.x, self.pt2.x, self.pt3.x)
	@property
	def width(self):
		return self.right-self.left
	@property
	def height(self):
		return self.top-self.bottom
	
	#punkty - wierzcholki bboxa
	@property
	def topleft(self):
		return Point(self.left, self.top)
	@property
	def bottomleft(self):
		return Point(self.left, self.bottom)
	@property
	def topright(self):
		return Point(self.right, self.top)
	@property
	def bottomright(self):
		return Point(self.right, self.bottom)

