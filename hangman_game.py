import random
from ascii_art import stages, HANGMANLOGO
from wordlist import word_list

print(HANGMANLOGO)

random_word = random.choice(word_list)
lives=len(stages)-1
go=False
blanks = []
obtain=""

for i in range(len(random_word)):
    blanks += "_"

while not go:
    letter = input("Guess a letter: ").lower()

    if letter in blanks:
        print(f"You've already guessed {letter}")
   
    for n in range(0,len(random_word)):
        if random_word[n]==letter:
            blanks[n] = letter

    print(blanks)
    if letter not in random_word:
        lives = lives-1
        if not lives==0:
            print(f"You guessed {letter}, that's not in the word. You lose a life.")
        print(stages[6-lives])
        if lives==0:
            go=True
            print(f"Game over.\n The word is {random_word}")
    else:
        print(stages[6-lives])
    if "_" not in blanks:
        go=True
        print("You Won!")

# else:
#     print("You lose.")
    # method 2:
    # for i in range(0,len(blanks)):
    #     if blanks[i]==random_word[i]:
    #         obtain=random_word
    #     else:
    #         obtain=blanks
