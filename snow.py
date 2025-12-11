import sys
import pygame
import random #dolosowego generowania atrybutów nowych snieżynek

pygame.init()
size = (width, height) = (960, 540)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("gra w śnieg")

fps = 60
clock = pygame.time.Clock()

#grupy sprite'ów (użyteczne w rysowaniu i liczeniu wyników)
unmelted = pygame.sprite.Group()
melted = pygame.sprite.Group()
fell = pygame.sprite.Group()

class Snowflake(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		#rozmiar recta
		self.image = pygame.Surface([30, 30])
		unmelted.add(self)
		self.color = (0,0,random.randint(180,255))
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.y = random.randint(-70, -30)
		self.rect.x = random.randint(30,width-30)
		self.vel = random.randint(1,2)

	
	def update(self):
		self.rect.y += self.vel


mouse_pos = (0, 0)

#pierwsza sniezynka, która jest od startu gry
Snowflake()

font = pygame.font.Font(None, 30)
game_over = False

#główna pętla
while True:

	#nadrzedna pętla
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

	#do restartowania gry po przegraniu
	if pygame.key.get_pressed()[pygame.K_r] and game_over == True:
			game_over=False
			unmelted.empty()
			melted.empty()
			fell.empty()
			Snowflake()
		
	
	#pętla gry
	while game_over==False:

		#wewnetrza petla po klikaniu na śnieżynki
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = event.pos

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
				#dwie nowe śniezynki
				Snowflake()
				Snowflake()
			
		#rysowanie wyniku
		roztopione = "ilosc roztopionych: {}".format(len(melted))
		text_surf = font.render(roztopione, True, (255,255,255))
		text_rect = text_surf.get_rect(center=(120, 20))
		screen.blit(text_surf, text_rect)
		
		

		#warunki końca gry
		if len(fell)>=10 or len(unmelted)==0:
			game_over=True
			#wychodzimy z petli
			break

		pygame.display.flip()
		clock.tick(fps)

	#komunikat o końcu gry
	screen.fill((0, 0, 20))
	koniec = "koniec gry, wynik: {}".format(len(melted))
	restartuj = "nacisnij {} aby sprobowac jeszcze raz".format("R")
	koniec_surf = font.render(koniec, True, (255,255,255))
	koniec_rect = koniec_surf.get_rect(center=(width // 2, height // 2))
	restartuj_surf = font.render(restartuj, True, (255,255,255))
	restartuj_rect = restartuj_surf.get_rect(center=(width // 2, height // 2 + 30))
	screen.blit(koniec_surf, koniec_rect)
	screen.blit(restartuj_surf, restartuj_rect)
	pygame.display.flip()


			
		
	
