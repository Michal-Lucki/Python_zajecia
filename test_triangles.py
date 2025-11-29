import pytest
from points_n import Point
from triangles_n2 import Triangle
from math import sqrt

p1=Point(1,4)
p2=Point(2,9)
p3=Point(-1,0)

trojkat=Triangle.from_points((p1, p2, p3))

def test_init():
	assert repr(trojkat)=="Triangle(1, 4, 2, 9, -1, 0)"
	assert str(trojkat)=="[(1, 4), (2, 9), (-1, 0)]"
	with pytest.raises(ValueError):
		#wspolliniowość
		Triangle(1,1,2,2,3,3)

def test_eq_ne():
	assert Triangle.from_points((p1, p2, p3))==Triangle.from_points((p2, p3, p1))
	assert trojkat!=trojkat.move(1,1)
	assert Triangle(7,0,4,-1,9,11)==Triangle.from_points((Point(9,11), Point(7,0), Point(4,-1)))

def test_area():
	assert Triangle(0,4,7,0,0,0).area==(4*7)/2
	#porównanie dwoch metod liczenia pola
	assert pytest.approx(trojkat.area, rel=0.001)==0.5*Point.cross(p1-p3, p2-p3)
	with pytest.raises(TypeError):
		#area nie jest już funkcją, tylko atrybutetm!! (@property)
		trojkat.area()

def test_center():
	#trojkat rownoboczny
	prb1=Point(-1,0)
	prb2=Point(1,0)
	prb3=Point(0,sqrt(3))
	trb=Triangle.from_points([prb1, prb2, prb3])
	assert trb.center==Point(0, sqrt(3)/3)
	#rowna odleglosc wierzcholkow od srodka trojkata rownobocznego
	assert Point.dist(prb1, trb.center)==Point.dist(prb2, trb.center) and Point.dist(prb2, trb.center)==Point.dist(prb3, trb.center)
	#srodek trojkata macierzystego rowny srodkowi trojkataa z srodków boków troj.macierz.
	assert trojkat.center==trojkat.make4()[3].center

def test_move():
	assert trojkat.area==trojkat.move(9,-11).area
	assert trojkat==trojkat.move(0,0)
	with pytest.raises(TypeError):
		#proba przesuniecia o inta
		trojkat.move(1)

def test_make4():
	assert isinstance(trojkat.make4(), tuple)
	laczna_powierzchnia=0
	for trg in trojkat.make4():
		laczna_powierzchnia+=trg.area

	#laczna powierzchnia czterech mniejszych rowna macierzystemu
	assert pytest.approx(trojkat.area, rel=0.0001)==laczna_powierzchnia
	#skladanie funkcji (najpierw move potem make4 == najpierw make4 potem move)
	assert trojkat.move(3,3).make4()==(trojkat.make4()[0].move(3,3), trojkat.make4()[1].move(3,3), trojkat.make4()[2].move(3,3), trojkat.make4()[3].move(3,3))

def test_bbox():

	assert isinstance(trojkat.bottom, int)
	assert trojkat.left==-1
	with pytest.raises(TypeError):
		trojkat.bottomright()



