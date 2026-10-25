player1 = input("Player1, enter your move(rock, paper or scissors): ").lower()
player2 = input("Player2, enter your move(rock, paper or scissors): ").lower()

valid_moves = ["rock", "paper", "scissors"]

if player1 not in valid_moves or player2 not in valid_moves:
    print("Error: Invalid input!")

elif player1 == player2:
    print("It's a tie!")

elif (player1 == "rock" and player2 == "scissors") or\
     (player1 == "scissors" and player2 == "paper") or\
     (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins!")

else:
    print("Player 2 wins!")