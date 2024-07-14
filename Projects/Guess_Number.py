import random


def guesser(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x} 😇: "))
        if guess < random_number:
            print("Sorry Guess Agin! Too Low 🔻")
        elif guess > random_number:
            print("Sorry Guess Agin! Too High 🔺")
    print(f"Yay 🥳 Congratulation! You Guessed The Number {random_number} correctly ✨")


guesser(50)
