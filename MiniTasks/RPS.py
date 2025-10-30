import random as rd

#Validates player_pick to check if the input is valid or invalid
def validatePlayerPick(player_pick):
    for i in picks:
        if player_pick == i:
            return True
    return False

#Compares the player_pick and computer_pick based on the rock, paper, scissors power system
def comparePicks(computer_pick, player_pick):
    computer_pick = computer_pick.lower()
    player_pick = player_pick.lower()

    if player_pick == computer_pick:
        return "tie"
    elif player_pick == picks[0] and computer_pick == picks[1]:
        return "computer"
    elif player_pick == picks[0] and computer_pick == picks[2]:
        return "player"
    elif player_pick == picks[2] and computer_pick == picks[1]:
        return "player"
    elif player_pick == picks[1] and computer_pick == picks[0]:
        return "player"
    elif player_pick == picks[2] and computer_pick == picks[0]:
        return "computer"
    elif player_pick == picks[1] and computer_pick == picks[2]:
        return "computer"
    
#Determines the result on whether the player wins, loses, or ties the game
def determineResult(result):

    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    elif result == "computer":
        print("You lose!")

#Shows the Game Result of the match. It shows the player_pick, computer_pick, and the result of the game.
def showResults():
    print("--- Game Result ---")
    print(f"You chose: {player_pick}")
    print(f"Computer chose: {computer_pick}")
    determineResult(comparePicks(computer_pick, player_pick))

#Asks the user if he/she continues to play
def continuePlay():

    while True:
        choice = input("\nDo you want to play again? (yes or no): ")
        choice = choice.lower()

        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print('Invalid choice!')
            continue

if __name__ == "__main__":
    print("Welcome to Rock, Paper, and Scissors!")
    while True:
        picks = ("rock", "paper", "scissors") #Picks to choose from

        computer_pick = rd.choice(picks) #Randomized computer_pick

        player_pick = input("Enter rock, paper, or scissors: ") #Asks for player_pick input

        if validatePlayerPick(player_pick) == False: #Validates player_pick input
            print("Invalid input!")
            continue
        
        showResults()#Shows the Game Result

        if continuePlay(): #Checks if the user wishes to continue playing
            continue
        else:
            print("Thanks for playing!")
            break
        

