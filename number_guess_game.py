from random import randint

def game(num):
    gnum = randint(1,100)
    game_over = False
    while not game_over:
        print(f"You have {num} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess!=gnum and num>1:
            if guess>gnum:
                print("Too high.")
            else:
                print("Too low.")
            print("Guess again.")
        num -= 1
        if num==0:
            print(f"You're out of guesse, you lose, the number is {gnum}.")
            game_over = True
        if guess==gnum:
            print(f"You got it. The number was {gnum}.")
            game_over=True


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'medium' or 'hard': ").lower()
if level=='hard':
    game(num=5)
elif level=="medium":
    game(num=7)
elif level=="easy":
    game(num=10)
else:
    print("Fuck you")