import random
number  = random.randint(1, 100)

while True:
    guess = input("Guess a number between 1 and 100 or Quit(Press Q if you wish to quit the game): ")

    if guess == "Q":
        print("You have quit the game!")
        break

    guess = int(guess)
    if guess == number:
        print("You have guessed the number!")
        break
    elif guess < number:
        print("Too Low!")
    else:
        print("Too High!")

print("--GAME OVER--")