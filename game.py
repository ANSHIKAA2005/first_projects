import random
while True:
    user_choice = input(f"\nEnter your choice (stone/paper/scissors): ").lower()
    possible_choices= ["stone", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    if user_choice not in possible_choices:
        print("Invalid input. Please enter stone, paper or scissors.")
        continue
    print("User chose", {user_choice}, "computer chose ",{computer_choice},".")
    if user_choice == computer_choice:
        print("Both players selected {user_choice}. It's a tie!")
    elif user_choice == "stone":
        if computer_choice == "scissors":
            print("Stone smashes scissors! You win!! :)")
        else:
            print("Paper covers stone! You lose.")
    elif user_choice == "paper":
        if computer_choice == "stone":
            print("Paper covers stone! You win!! :)")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!! :)")
        else:
            print("Stone smashes scissors! You lose.")
    play_again = input("Play again? (yes/no): \n").lower()
    if play_again != "yes":
        break
print("\nTHANKYOU !!! :)")



