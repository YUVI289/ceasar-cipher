import random

def deal():
    cards = [11,2,3,4,5,6,7,8,9,10,1,1,1]
    card = random.choice(cards)
    return card

def score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21 and len(cards)==2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
        
def game():
    user_cards = []
    comp_cards = []
    
    game_over = False
    for i in range(2):
        user_cards.append(deal())
        comp_cards.append(deal())
    while not game_over:
        print(f"Your cards: {user_cards}, and your score is {score(user_cards)}")
        print(f"Computer's first hand: {comp_cards[0]}")
        if score(user_cards)==0 or score(comp_cards)==0 or score(user_cards)>21:
            game_over = True
        else:
            choice1 = input("Type 'y' for another card, and 'n' to stop dealing: ").lower()
            if choice1=="y":
                user_cards.append(deal())
            else:
                game_over=True

    while score(comp_cards) != 0 and score(comp_cards) < 17:
        comp_cards.append(deal())

    print(f"   Your final hand: {user_cards}, final score: {score(user_cards)}")
    print(f"   Computer's final hand: {comp_cards}, final score: {score(comp_cards)}")
    print(compare(score(user_cards), score(comp_cards)))

while input("BlackJack.\nIf you want to play press 'y': ").lower()=='y':
    game()