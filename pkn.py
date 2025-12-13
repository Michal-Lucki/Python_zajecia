import tkinter as tk
import random

root = tk.Tk()

root.title("papier-kamień-nożyce")

root.configure(width=1400, height=900)
root.resizable(width=False, height=False)


#wstepne ustawienia zmiennych gry
score = None

player_move = None
#mozliwe ruchy komputera
computer_moves = ("P", "K", "N")
computer_move = None

player_display = tk.Label(root, text=player_move, font="Times 14")
comp_display = tk.Label(root, text=computer_move, font="Times 14")
score_display = tk.Label(root, text=score, font="Times 14")


#funkcja aktywowana po przycisku
def player_moved(move):

	#globale, żebyzachować te same zmienne
	global player_move, computer_move, score

	player_move = move
	computer_move=""
	player_display.config(text=player_move)
	comp_display.config(text=computer_move)
	player_display.grid(row=1, column=0)

	#sztuczne "oczekiwanie" na ruch komputera
	root.after(300)

	#losowe wybór komputeea
	computer_move = computer_moves[random.randint(0,2)]
	comp_display.config(text=computer_move)
	comp_display.grid(row=1, column=1)

	

	#wynik rozgrywki
	if player_move=="P":
		if computer_move=="P":
			score="remis"
		elif computer_move=="K":
			score="wygrana"
		elif computer_move=="N":
			score="przegrana"
	elif player_move=="K":
		if computer_move=="P":
			score="przegrana"
		elif computer_move=="K":
			score="remis"
		elif computer_move=="N":
			score="wygrana"
	elif player_move=="N":
		if computer_move=="P":
			score="wygrana"
		elif computer_move=="K":
			score="przegrana"
		elif computer_move=="N":
			score="remis"

	#wyswietla wynik
	score_display.config(text=score)


#przyciski gracza
player_p = tk.Button(root, text= "papier", command=lambda: player_moved("P"))
player_k = tk.Button(root, text= "kamień", command=lambda: player_moved("K"))
player_n = tk.Button(root, text= "nożyce", command=lambda: player_moved("N"))




player_p.grid(row=2, column=0)
player_k.grid(row=2, column=1)
player_n.grid(row=2, column=2)
score_display.grid(row=0, column=0, columnspan=2)

root.mainloop()