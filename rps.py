import random 

def main():
    print("Welcome to Rock Paper Scissors!")
    print()
    print("The rules of Rock Paper Scissors, which (for those of you who don’tknow) are as follows:")
    print(f'1. Two players secretly pick one of “rock,” “paper,” or “scissors.”')
    print("2. Both players reveal their selection to the other player at once")
    print("3. And  the winner is chosen based on what the selections are")
    print("4. Rock beats scissors (by crushing them)")
    print("5. scissors beats paper (by cutting it")
    print("6. paper beats rock (by covering it)")
    print("7. If both players select the same one, it is a tie.")
    print()

    choices = ["rock", "paper", "scissors"]
    round_number = 1

    while True:
        print(f"--- Round {round_number} ---")

        player_choice = input("Enter your choice (rock, paper, or scissors): ")
        computer_choice = random.choice(choices)
        print("You selected:", player_choice)
        print("Computer selected:", computer_choice)
        if player_choice == computer_choice:
            print("It is a tie!, Rematching ")
            print()
            round_number += 1
            continue
        elif(
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You Wins!")
        else:
            print("Computer Wins!")

        break
    

if __name__ == "__main__":
    main()