import unittest

class Node:

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

	def __eq__(self, other):
		return self.data==other.data

	def __ne__(self, other):
		return not self.data==other.data

class SingleList:

	def __init__(self):
		self.length = 0
		self.head = None
		self.tail = None

	#iterator w trybie generatora
	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

	#wprowadzam str do latwego wyswietlania list
	def __str__(self):
		string=[]
		for x in self:
			string.append(str(x))

		", ".join(string)
		return str(string)

	def is_empty(self):
		return self.head is None

	def count(self):
		return self.length

	def insert_head(self, node):
		#jesli lista jest niepusta
		if self.head:
			#przesuwamy head
			node.next = self.head
			self.head = node
		#jesli lista jest pusta (self.head==None)
		else:
			#jedyny element (zarówno head i tail)
			self.head = self.tail = node

		#aktualizacja dlugosci listy
		self.length+=1

	def insert_tail(self, node):
		#jesli lista jest niepusta
		if self.head:
			#przesuniecie
			self.tail.next = node
			self.tail = node
		#jesli lista pusta
		else:
			#jedyny element (zarówno head i tail)
			self.head = self.tail = node
		
		#aktualizacja dlugosci
		self.length+=1

	def remove_head(self):
		if self.is_empty():
			#nie ma z czego usuwac
			raise ValueError("lista jest pusta!")

		node = self.head
		if self.length==1:
			#czyscimy liste całkiem
			self.head = self.tail = None
		else:
			#przesuniecie
			self.head = self.head.next
		#czysczenie head'a
		node.next = None

		#aktualizacja dlugosci
		self.length-=1

		#zwrócenie usunietego head'a
		return node

	""" metody dodane dla zadania 11.2 """

	def search(self, data):
		#w wartosci self.node_id zapisuje polozenie szukanego wezla w liscie
		self.node_id = -1
		found=False
		for node in self:
			self.node_id+=1
			if node.data==data:
				#toggle, zeby obsluzyc wyjątek nizej
				found=True
				#zwracam wezel
				return node
				break

		if found==False:
			#wyrzuca blad w przypadku braku wezla o szukanej wartości
			raise ValueError("brak węzła o podanej zawartości.")

		"""poniewaz petla po kazdym węźle, to klasa O(n)"""

	def find_min(self):
		#zmienna val przechowuje najnizsza wartosc dla kolejnych wezlow
		val=self.head.data
		for node in self:
			#jesli wartosc wezla mniejsza niz dotychczasowa najznizsza,
			#to zamieniam
			if node.data<val:
				val=node.data

		return val

		"""poniewaz petla po kazdym węźle, to klasa O(n)"""

	def find_max(self):
		#zmienna val przechowuje najwieksza wartosc dla kolejnych wezlow
		val=self.head.data
		for node in self:
			#jesli wartosc wezla mniejsza niz dotychczasowa najznizsza,
			#to zamieniam
			if node.data>val:
				val=node.data

		return val

		"""poniewaz petla po kazdym węźle, to klasa O(n)"""

	def reverse(self):
		rev_list=SingleList()
		for node in self:
			#tworze nowy node, aby nie zepsuc starych
			#kiedy nie uzywalem nowych, "nadpisywalem" stare wezly,
			#ktore mialy juz swoje node.next

			rev_node=Node(node.data)
			rev_list.insert_head(rev_node)

			#nie jest to rozwiazanie najbardziej optymalne,
			#ale jedyne na jakie wpadlem

		return rev_list


""" testy """

class TestNode(unittest.TestCase):

	def setUp(self):

		#node testowy: Node(-5)
		self.node_testowy=Node(-5)

	def test_init(self):
		self.assertEqual(self.node_testowy.data, -5)
		#pusty next
		self.assertTrue(self.node_testowy.next==None)

	def test_str(self):
		self.assertEqual(str(self.node_testowy), "-5")
		self.assertEqual(str(self.node_testowy), str(self.node_testowy.data))

	def test_eq(self):
		self.assertTrue(self.node_testowy==Node(-5))
		#blad porownywania inta do węzła...
		with self.assertRaises(AttributeError):	
			self.assertTrue(self.node_testowy==-5)

		#...co innego atrybut data (patrzz test_init)

	def test_neq(self):
		self.assertFalse(self.node_testowy==Node(95))

class TestSlist(unittest.TestCase):

	def setUp(self):

		#lista testowa: ['-3', '7', '2']
		self.lista_testowa=SingleList()
		self.lista_testowa.insert_head(Node(7))
		self.lista_testowa.insert_tail(Node(2))
		self.lista_testowa.insert_head(Node(-3))

		#lista pusta: []
		self.lista_pusta=SingleList()

	def test_init(self):
		self.assertEqual(self.lista_testowa.head.data, -3)
		self.assertEqual(self.lista_testowa.tail.data, 2)
		self.assertEqual(self.lista_testowa.length, 3)

		#dla listy pustej
		self.assertEqual(self.lista_pusta.head, self.lista_pusta.tail)
		self.assertEqual(self.lista_pusta.head, None)
		self.assertEqual(self.lista_pusta.length, 0)

	def test_iter(self):
		nodes_data=[]
		for node in self.lista_testowa:
			nodes_data.append(node.data)

		self.assertTrue(nodes_data==[-3,7,2])

	def test_str(self):
		self.assertEqual(str(self.lista_testowa), "['-3', '7', '2']")
		
		#dla listy pustej
		self.assertEqual(str(self.lista_pusta), "[]")

	def test_is_empty(self):
		self.assertFalse(self.lista_testowa.is_empty())

		#dla listy pustej
		self.assertTrue(self.lista_pusta.is_empty())

	def test_count(self):
		#jest to zwykly interfejs do odczytu (self.length)
		self.assertEqual(self.lista_testowa.length, self.lista_testowa.count())
		self.assertEqual(self.lista_pusta.length, self.lista_pusta.count())

	def test_insert_head(self):
		wezel=Node(8)
		#dodaje wezel o wartosci 8 do listy testowej
		self.lista_testowa.insert_head(wezel)
		self.assertEqual(self.lista_testowa.head, wezel)
		#sprawdzam, czy atrybut dlugosci listy sie zmienil
		self.assertEqual(self.lista_testowa.length, 4)
		#wyjatek dla proby dodania inta zamiastt węzła (node(4))
		with self.assertRaises(AttributeError):
			self.lista_testowa.insert_head(4)

	def test_insert_tail(self):
		wezel=Node(11)
		self.lista_testowa.insert_tail(wezel)
		self.assertEqual(self.lista_testowa.tail, wezel)

		#dla pustej listy
		self.lista_pusta.insert_tail(wezel)
		#skoro pusta, to head jest jednoczesnie tailem
		self.assertEqual(self.lista_pusta.head, wezel)

	def test_remove_head(self):
		self.lista_testowa.remove_head()
		#['-3', '7', '2'] --> ['7', '2']
		self.assertEqual(self.lista_testowa.head.data, 7)
		#sprawdzam aktualizacje atrybutu length
		self.assertEqual(self.lista_testowa.count(), 2)

		#sprawdzam wprowadzony wyjatek dla pustej listy ("lista jest pusta!")
		with self.assertRaises(ValueError):
			self.lista_pusta.remove_head()

	def test_search(self):
		#sprawdzam node
		szukany_node=self.lista_testowa.search(7)
		self.assertEqual(szukany_node, Node(7))
		#sprawdzam node_id (dopiero po wywolaniu .search()!)
		self.assertEqual(self.lista_testowa.node_id, 1)

		#sprawdam wprwoadzony wyjątek dla braku szukanej wartosci
		with self.assertRaises(ValueError):
			self.lista_pusta.search(420)

	def test_min_max(self):
		self.assertEqual(self.lista_testowa.find_min(), -3)
		self.assertEqual(self.lista_testowa.find_max(), 7)

		#dla pustej listy
		with self.assertRaises(AttributeError):
			self.lista_pusta.find_min()
			self.lista_pusta.find_max()

	def test_reverse(self):
		odwrocona_lista_testowa=self.lista_testowa.reverse()
		#"head to tail" - zamiana heada na tail
		self.assertEqual(self.lista_testowa.head, odwrocona_lista_testowa.tail)
		self.assertEqual(odwrocona_lista_testowa.head.data, 2)

		#nie zmienia sie dlugosc
		self.assertEqual(self.lista_testowa.length, odwrocona_lista_testowa.length)

if __name__=='__main__':
	unittest.main()
