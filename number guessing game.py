import random

print("=" * 45)
print("Welcome to the number guessing game")
print("=" * 45)
print("Try to guess what the computer guesses")
print("Choose numbers between 1 to 10")
print("Type 'stop' to quit anytime from the game")
print("-" * 45)

games_played = 0
wins = 0

while True:
    guess = input("\nEnter your guess: ")

    if guess.lower() == "stop":
        print("\n" + "=" * 45)
        print("Thanks for playing!")
        print("Games played:", games_played)
        print("Games won:", wins)
        print("-" * 45)
        break

    try:
        guess = int(guess)

        if guess > 10 or guess < 1:
            print("Please enter a number between 1 and 10")

        else:
            number = random.randint(1, 10)
            games_played += 1

            print("The computer's number was", number)

            if guess == number:
                print("You win! Great success")
                wins += 1

            else:
                print("You lose! Better luck next time")

    except ValueError:
        print("Please enter a valid number")

print("Hello")
    
    

