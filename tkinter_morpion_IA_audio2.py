import tkinter as tk
from tkinter import messagebox
import random
import pygame 

# Variables globales
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'momo'
vs_ai = False

# Initialiser pygame 
pygame.init() 

# Charger le son 
son_clic = pygame.mixer.Sound("click.wav") 

# Fonction pour jouer le son de clic 
def jouer_son(): 
    son_clic.play()

# Cette foction vérifie si le joueur spécifié a gagné le jeu :
def check_winner(board, player):
    # Vérifie chaque ligne: Si toutes les cellules d'une ligne sont occupées par le même joueur.
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Vérifie chaque colonne: Si toutes les cellules d'une colonne sont occupées par le même joueur.   
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Vérifie les diagonales: Si toutes les cellules de la diagonale principale ou secondaire sont occupées par le même joueur.   
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Cette fonction détermine le meilleur coup pour l'IA en utilisant l'algorithme Minimax.
def ai_move(board):
    # Initialisation: best_score est initialisé à moins l'infini pour trouver le score maximal.
    best_score = -float('inf')
    move = None
    #Simulation des coups: Parcourt toutes les cellules vides et simule le coup de l'IA ('IA').
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'IA'
                # Appel de Minimax: Utilise l'algorithme Minimax pour évaluer chaque coup.
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    # Mise à jour du meilleur coup: 
                    # Si le score est meilleur que le score actuel, met à jour best_score et move.
                    best_score = score
                    move = (i, j)
    if move:
        return move
    
# Cette fonction évalue chaque position du jeu en utilisant l'algorithme Minimax.
def minimax(board, depth, is_maximizing):
    #Conditions de fin: Vérifie si un joueur a gagné ou si le jeu est un match nul.
    winner = check_winner(board, 'momo')
    if winner:
        return -1
    winner = check_winner(board, 'IA')
    if winner:
        return 1
    if all(cell != ' ' for row in board for cell in row):
        return 0
    # Maximisation pour l'IA ('IA'): Cherche le score maximum possible pour l'IA.
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'IA'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    # Minimisation pour l'adversaire ('momo'): Cherche le score minimum possible pour l'adversaire.
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'momo'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Cette fonction crée et gère l'interface utilisateur avec Tkinter.
def create_widgets(root):
    global board_buttons, label
    label = tk.Label(root, text="Joueur 1 (momo)")
    label.grid(row=0, column=0, columnspan=3)
    board_buttons = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            board_buttons[i][j] = tk.Button(root, text='', font=('normal', 40, 'normal'), width=5, height=2, command=lambda row=i, col=j: on_click(row, col))
            board_buttons[i][j].grid(row=i+1, column=j)
    reset_button = tk.Button(root, text="Réinitialiser", command=reset_board)
    reset_button.grid(row=4, column=0, columnspan=3)
    ai_button = tk.Button(root, text="Jouer contre IA", command=toggle_ai)
    ai_button.grid(row=5, column=0, columnspan=3)

# Cette fonction gère l'état du jeu (réinitialisation, basculement de l'IA, clics des joueurs).
def reset_board():
    global board, current_player, vs_ai
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            board_buttons[i][j].config(text='', state=tk.NORMAL)
    current_player = 'momo'
    label.config(text="Joueur 1 (momo)")

# Cette fonction bascule entre le mode de jeu contre un autre joueur humain et le mode de jeu contre l'IA
def toggle_ai():
    global vs_ai # La fonction peut modifier la variable vs_ai définie en dehors de cette fonction
    vs_ai = not vs_ai # Basculer le var. si False (mode deux joueurs), il devient True (mode contre IA), et inversement.
    reset_board() # appelle reset_board() initialiser le plateau de jeu
    if vs_ai: # Si vs_ai est True, pour indiquer que le joueur 1 joue contre l'IA
        label.config(text="Joueur 1 (momo) vs IA (IA)")
    else: # Si vs_ai est False, pour indiquer que le jeu est en mode deux joueurs humains
        label.config(text="Joueur 1 (momo) vs joueur 2 (flor)")

# Cette fonction gère les clics des joueurs sur la grille avec l'appel de fonction du son
def on_click(row, col):
    global board, current_player
    if board[row][col] == ' ':
        # Jouer le son de clic
        jouer_son()

        board[row][col] = current_player
        board_buttons[row][col].config(text=current_player)
        if check_winner(board, current_player):
            messagebox.showinfo("Gagné!", f"Le joueur {current_player} a gagné!")
            reset_board()
        elif all(cell != ' ' for row in board for cell in row):
            messagebox.showinfo("Match nul", "C'est un match nul!")
            reset_board()
        else:
            current_player = 'IA' if current_player == 'momo' else 'momo'
            label.config(text=f"Joueur {current_player} ({current_player})")
            if current_player == 'IA' and vs_ai:
                move = ai_move(board)
                if move:
                    on_click(move[0], move[1])

# Initialisation de l'application Tkinter et crée les widgets.
root = tk.Tk()
root.title("TIC TAC TOE")
create_widgets(root)
root.mainloop() # démarrer la boucle principale de l'application graphique

# Arrêter le son
pygame.quit()