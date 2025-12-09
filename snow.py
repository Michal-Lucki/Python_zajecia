import sys
import pygame
import random #dolosowego generowania atrybutów nowych snieżynek

pygame.init()
size = (width, height) = (960, 540)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("gra w śnieg")

fps = 60
clock = pygame.time.Clock()

unmelted = pygame.sprite.Group()
melted = pygame.sprite.Group()
fell = pygame.sprite.Group()

class Snowflake(pygame.sprite.Sprite):

	def __init__(self, color):
		super().__init__()
		self.image = pygame.Surface([30, 30])
		self.add(unmelted)
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.y = -50
		self.rect.x = random.randint(30,width-30)
		self.vel = random.randint(1,2)

	
	def update(self):
		self.rect.y += self.vel


	
#funkcja do generowania śniezynekk
#def new_snowflake():
#	snowflake = pygame.Rect(random.randint(30, width-30), -50, 30, 30)
#	return snowflake

#lista obiektów (sniezynek); na starcie dziesiec
#objects = [new_snowflake() for x in range(10)]
#lista szybkosci spadania sniezynek (losowe)
#objects_velocities = [random.randint(1, 2) for x in objects]
#lista kolorow sniezynek
#objects_colors = [random.randint(180, 255) for x in objects]

mouse_pos = (0, 0)

Snowflake((0,0,255))

font = pygame.font.Font(None, 30)
game_over = False

#główna pętla
while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
	
	
	#pętla gry
	#while not game_over:


		#rysowanie obrazu
	screen.fill((0, 0 ,90))
	unmelted.draw(screen)
	unmelted.update()
		

		#liczenie (i usuwanie) tych co spadły (lub zostały roztopione)
	for snowflake in unmelted:
		
		#print (snowflake.rect.y)
		if snowflake.rect.y>height:
			unmelted.remove(snowflake) #ewentualnie kill gduby bylo wiecej grup
			fell.add(snowflake)
		if snowflake.rect.collidepoint(mouse_pos):
			unmelted.remove(snowflake)
			melted.add(snowflake)
			Snowflake((0,0,255))
			Snowflake((0,0,255))
		
		#rysowanie wyniku
	roztopione = "ilosc roztopionych: {}".format(len(melted))
	text_surf = font.render(roztopione, True, (255,255,255))
	text_rect = text_surf.get_rect(center=(120, 20))
	screen.blit(text_surf, text_rect)
	
	

		#warunek końca gru
	if len(fell)==10:
		game_over=True
		
	pygame.display.flip()
	clock.tick(fps)

	screen.fill((0, 0, 20))
	koniec = "koniec gry, wynik: {}".format(len(melted))
	text_surf = font.render(koniec, True, (255,255,255))
	text_rect = text_surf.get_rect(center=(width // 2, height // 2))
	screen.blit(text_surf, text_rect)

