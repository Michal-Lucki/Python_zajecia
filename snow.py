import sys
import pygame
import random #dolosowego generowania atrybutów nowych snieżynek

pygame.init()
size = (width, height) = (960, 540)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("gra w śnieg")

fps = 60
clock = pygame.time.Clock()

#funkcja do generowania śniezynekk
def new_snowflake():
	snowflake = pygame.Rect(random.randint(30, width-30), -50, 30, 30)
	return snowflake

#lista obiektów (sniezynek); na starcie dziesiec
objects = [new_snowflake() for x in range(10)]
#lista szybkosci spadania sniezynek (losowe)
objects_velocities = [random.randint(1, 2) for x in objects]
#lista kolorow sniezynek
objects_colors = [random.randint(180, 255) for x in objects]

mouse_pos = (0, 0)
melt_counter = 0
fell_counter = 0
font = pygame.font.Font(None, 30)
game_over = False

#główna pętla
while True:

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)

	#pętla gry
	while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos

		#uzywam enumerate zeby przypisac id sniezynce
		for obj in objects:
			#usuwanie sniezynki
			if obj is None:
				continue
			if obj.collidepoint(mouse_pos):
				#usuwam zarowno sniezynke jak i jej predkosc
				obj_id=objects.index(obj)
				objects.pop(obj_id)
				objects_velocities.pop(obj_id)
				objects_colors.pop(obj_id)
				#doliczamy do countera
				melt_counter+=1
				#pojawiają sie dwie nowe z prędkościami jeden
				objects.append(new_snowflake())
				objects_velocities.append(random.randint(1, 3))
				objects_colors.append(random.randint(180, 255))
				objects.append(new_snowflake())
				objects_velocities.append(random.randint(1, 3))
				objects_colors.append(random.randint(180, 255))

		#rysowanie obrazu
		screen.fill((0, 0 ,90))
		for i, obj in enumerate(objects):
			pygame.draw.rect(screen, (0, 0, objects_colors[i]), obj)
			
			#ruch sniezynki
			if objects_velocities[i] == 0:
				continue

			obj.y+=objects_velocities[i]

		#liczenie (i usuwanie) tych co spadły
		for obj in objects:
			if obj.y>height:
				obj_id=objects.index(obj)
				objects.pop(obj_id)
				objects_velocities.pop(obj_id)
				objects_colors.pop(obj_id)
				fell_counter+=1

		#rysowanie wyniku
		roztopione = "ilosc roztopionych: {}".format(melt_counter)
		text_surf = font.render(roztopione, True, (255,255,255))
		text_rect = text_surf.get_rect(center=(120, 20))
		screen.blit(text_surf, text_rect)


		pygame.display.flip()
		clock.tick(fps)

		#warunek końca gru
		if fell_counter==10:
			game_over=True

	screen.fill((0, 0, 20))
	koniec = "koniec gry, wynik: {}".format(melt_counter)
	text_surf = font.render(koniec, True, (255,255,255))
	text_rect = text_surf.get_rect(center=(width // 2, height // 2))
	screen.blit(text_surf, text_rect)

	pygame.display.flip()