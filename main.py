#Tableau de tableaux représentant une grille 3x3
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
currentPlayer = "X"
turns = 0

#Affiche la grille gameBoard de manière formatée; Une boucle va s'exécuter trois fois, ce qui correspond à chaque ligne de la grille. 
#Une seconde boucle intérieure permet de sélectionner la colonne. La combinaison des deux boucles permet donc de sélectionner chaque case de la grille.
def printGameBoard():
  for indexRows in range(3):
    print("\n|---|---|---|")
    print("|", end="")
    for indexColumns in range(3):
      print("", gameBoard[indexRows][indexColumns], end=" |") #end permet de remplacer le saut de ligne après un print par le caractère de notre choix, ici | pour formater la grille.
  print("\n|---|---|---|")

#Met à jour la grille gameBoard avec le symbole du joueur dans la case choisie.
#number -=1 permet d'avoir le bon index comme il s'agit d'un array.
def modifyArray(number, playerSign):
  number -= 1
  if(number == 0):
    gameBoard[0][0] = playerSign
  elif(number == 1):
    gameBoard[0][1] = playerSign
  elif(number == 2):
    gameBoard[0][2] = playerSign
  elif(number == 3):
    gameBoard[1][0] = playerSign
  elif(number == 4):
    gameBoard[1][1] = playerSign
  elif(number == 5):
    gameBoard[1][2] = playerSign
  elif(number == 6):
    gameBoard[2][0] = playerSign
  elif(number == 7):
    gameBoard[2][1] = playerSign
  elif(number == 8):
    gameBoard[2][2] = playerSign

#Vérifie si le nombre sélectionné est déjà occupée ou non.
def checkSlot(number):
    number -= 1  
    row = number // 3
    col = number % 3
    if (isinstance(gameBoard[row][col], int)):
        return True
    else:
        print("La case est déjà occupée.")
#Permet de changer de joueur. Cette fonction est appelée après un tour
def switchPlayer(currentPlayer):
    if currentPlayer == "X":
        return "O"
    else:
        return "X"
    
#Vérifie les conditions de victoire
def checkWinner():
    #Vérifie si il y a trois X ou trois O alignés horizontalement.
    for row in gameBoard:
        if row[0] == row[1] == row[2] and isinstance(row[0], str): 
            return row[0]
        
    #Vérifie si il y a trois X ou trois O alignés verticalement.
    for col in range(3):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col] and isinstance(gameBoard[0][col], str):
            return gameBoard[0][col]

    #Vérifie si il y a trois X ou trois O alignés en diagonale
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] and isinstance(gameBoard[0][0], str):
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] and isinstance(gameBoard[0][2], str):
        return gameBoard[0][2]
    return
    
#Affiche le tableau à chaque tour pour suivre la progression de la partie. Chaque joueur doit sélectionner un nombre entre 1 et 9, correspondant à chaque case de la grille.  On modifie le tableau gameBoard avec le signe du joueur.
#On incrémente le nombre de tours de 1, puis on change de joueur.
while turns < 9:
    printGameBoard()
    try:
      slotNumber = int(input(f"(Tour de {currentPlayer}) Saisissez un nombre entre 1 et 9: "))
      if(slotNumber >=1 and slotNumber <=9 and checkSlot(slotNumber)):
          modifyArray(slotNumber, currentPlayer)
          turns +=1
          winner = checkWinner()  # Vérifie si un joueur a gagné
          if winner:
              print(f"Félicitations, le joueur {winner} a gagné !")
              printGameBoard()
              break  # Fin de la partie si un joueur a gagné
          currentPlayer = switchPlayer(currentPlayer)
      else:
          print("Erreur: La case est déjà utilisée ou vous n'avez pas sélectionné une valeur entre 1 et 9")
    except ValueError:
      print("Erreur: Vous devez entrer un nombre entre 1 et 9")
if turns == 9 and not winner: 
    print("Match nul !")
