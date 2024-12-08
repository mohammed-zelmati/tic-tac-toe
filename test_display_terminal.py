

# ====// Mohammed ZELMATI \\====

# instructions to the players and demonstration of the scheme with the numbers that must be return
#les instructions aux joueurs et démonstration de schéma avec les nombres qui doivent les rentrer
instructions = """ This will be our tic tac toe board

| 1 | 2 | 3 |

| 4 | 5 | 6 |

| 7 | 8 | 9 |

*instructions :
1. Insert the spot number(1,9) to put your sign,
2. You must fill all 9 spots to get result,
3. Player 1 will go first
"""

sign_dict =[] # Creating an empty list (création une liste vide) 
#loop to add a max of 9 values on sign_dict 
#boucle pour additionner max 9 valeurs sur sign_dict
for i in range(9):
    sign_dict.append("")

# Interface diagram function displayed on the terminal 
# fonction de schéma d'interface affiché sur le terminal
def print_board(sign_dict):
    board =f"""
        | {sign_dict[0]} | {sign_dict[1]} | {sign_dict[2]} |
        
        | {sign_dict[3]} | {sign_dict[4]} | {sign_dict[5]} |
        
        | {sign_dict[6]} | {sign_dict[7]} | {sign_dict[8]} |
         """  
    print(board)

index_list = [] # Creating an empty list 

# creation of a function that asks players to type numbers between 1 and 9, and assign its numbers to the index_list
# création d'une fonction qui demande aux joueurs de taper des nombres entre 1 et 9, et affecter ses nombres à la liste index_list
def take_input(player_name):
    while True :
        try:
            x  = int(input(f'{player_name} : '))
            x -= 1
            if 0 <= x < 10:
                if x in index_list:
                    print("this spot is blocked.")
                    continue
                index_list.append(x)
                return x
            print("Please enter number between 1-9")
        except ValueError:
            print("Entrée invalide,Veuillez entrer un entier") 

# creation of the function that designates the winner
# création la fonction qui désigne le vainqueur  
def result_winner(sign_dict, player_one, player_two):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # lignes verticales
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    
    for combo in winning_combinations:
        if all(sign_dict[i] == 'X' for i in combo):
            print(f"Congratulations {player_one}. You WON.!!")
            quit("Thank you both for joining")
        elif all(sign_dict[i] == 'O' for i in combo):
            print(f"Congratulations {player_two}. You WON.\n Vous avez gagné.!!")
            quit("Thank you both for joining")
    
    return
#creation The function that manages the game and orders the players and declares the winner or the game is tie
# création la fonction qui gère le jeu et qui ordonne les joueurs et qui déclare le vainqueur ou le jeu est à égalité
def main():
    print("Welcome to GAME :|=== TIC TAC TOE ===|")
    player_one = input("Enter player 1 name : ")
    player_two = input("Enter player 2 name : ")

    print(f"Thank you for joining Mr./Mrs. {player_one}  and Mr./Mrs. : {player_two}")
    print(instructions)
    print(f"Mr. {player_one}'s sign is - X")
    print(f"Mr. {player_two}'s sign is - O")
    print_board(sign_dict)
    for i in range(0,9):
        if i %2 == 0:
            index = take_input(player_one)
            sign_dict[index] = 'X'
        else :
            index = take_input(player_two)
            sign_dict[index] = 'O'

        print_board(sign_dict)
        result_winner(sign_dict, player_one, player_two)
    print("This is a tie..!! No body won. Play Again.")
    
# The call of the main() function to execute the game
# L'appelle de la fonction main() pour éxecute le jeu
main()   