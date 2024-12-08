import math # module standard sert aux calculs en mathématiques 

# Fonction affiche un interface de jeu sur le terminal
def print_board(board):
    for row in board:
        print(" | ".join(row),"|")
    print()

# fonction vérifie le vainqueur de jeu
def check_winner(board):
    # Vérification d'alignement
    for row in board:
        # Vérifie les lignes
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
        # Vérifie les colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def minimax(board, depth, is_maximizing):

    # Cette section vérifie si le jeu est terminé. Si le joueur 'X' gagne, on retourne -1,
    #  si 'O' gagne, on retourne 1, et si c'est un match nul, on retourne 0.
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif all(cell != ' ' for row in board for cell in row):
        return 0
    
    # phase de maximisation :Quand c'est au tour du joueur maximisant ('O'),
    #  l'algorithme essaie de trouver le meilleur score possible en explorant tous les coups possibles.
    #  best_score est initialement très bas (moins l'infini), et il est mis à jour avec le meilleur score trouvé.
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    
    # Phase de minimisation : Quand c'est au tour du joueur minimisant ('X'),
    #  l'algorithme essaie de trouver le pire score possible pour l'adversaire 
    # en explorant tous les coups possibles. best_score est initialement très élevé (plus l'infini),
    #  et il est mis à jour avec le pire score trouvé.
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# fonction de manipulation de joueur 'O' qui répésente IA
def best_action(board):
    # On initialise best_score à moins l'infini pour s'assurer que tout score trouvé 
    # sera supérieur à cette valeur initiale. 'move' est initialisé à None et sera mis à jour 
    # avec les meilleures coordonnées de mouvement trouvées.
    best_score = -math.inf
    move = None

    # Les deux boucles for parcourent toutes les cases de la grille.
    # Si une case est vide (' '), le joueur 'O' essaie de jouer dans cette case.
    # La fonction minimax est alors appelée pour évaluer le résultat de ce coup, 
    # avec une profondeur initiale de 0 et en indiquant que ce n'est plus au tour 
    # du joueur maximisant (False pour le joueur 'X').
    # Après l'appel à minimax, la case est réinitialisée (board[i][j] = ' ').
    # Si le score retourné par minimax est supérieur au best_score actuel, 
    # on met à jour best_score et on mémorise les coordonnées de ce coup 
    # comme étant le meilleur mouvement trouvé jusqu'à présent.
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    # retourne les coordonnées (i, j) du meilleur coup pour le joueur 'O'.               
    return move

# gère le jeu de morpion en alternant les tours entre le joueur et l'IA, 
# en vérifiant les conditions de victoire et de match nul après chaque tour.
def main():
    # La grille du jeu est initialisée comme une liste de listes, représentant une grille de 3x3 cases, toutes vides (' ').
    # La fonction print_board est appelée pour afficher la grille initiale.
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    #Une boucle infinie commence, ce qui permet au jeu de continuer jusqu'à ce qu'il y ait un gagnant ou un match nul.
    while True:
        
        # Tour du joueur :Le joueur entre son mouvement en spécifiant la ligne et la colonne.
        # Si la case choisie est vide (' '), le mouvement est validé en plaçant un 'X' dans cette case.
        # Si la case est déjà prise, un message d'erreur est affiché et le joueur doit réessayer.
        row, col = map(int, input("Enter your move (row and column):exemple: 0 1 : ").split())
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Invalid move. Try again.")
            continue
        print_board(board)  

        # La fonction check_winner est appelée pour vérifier si le joueur 'X' a gagné.
        # Si un gagnant est trouvé, un message de victoire est affiché et la boucle se termine.
        # Si toutes les cases sont remplies et qu'il n'y a pas de gagnant, un message de match nul est affiché et la boucle se termine.
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        elif all(cellule != ' ' for row in board for cellule in row):
            print("It's a tie!")
            break

        # Tour de l'IA : La fonction best_action est appelée pour déterminer le meilleur coup pour l'IA (joueur 'O').
        # Si une action est disponible, l'IA joue son coup en plaçant un 'O' dans la case correspondante.
        action = best_action(board)
        if action:
            board[action[0]][action[1]] = 'O'
        print_board(board)

        # Après le coup de l'IA, la fonction check_winner est de nouveau appelée pour vérifier si l'IA a gagné.
        # Les mêmes vérifications de victoire ou de match nul sont effectuées comme après le tour du joueur. 
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        elif all(cell != ' ' for row in board for cell in row):
            print("It's a tie!")
            break

# Appel de fonction main() pour executer le jeu programmé.
main()