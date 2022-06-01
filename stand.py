import random
from sum_return import *

card_stack = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K')

def stand(my_cards, dealers_cards):
    dealers_cards.append(random.sample(card_stack, 1))
    print("------------------------------------")
    print("Your Cards --> {} --> {}".format(my_cards, sum_return_self(my_cards))) 
    print("Delaers Cards --> {} --> {}".format(dealers_cards, sum_return_dealer(dealers_cards)))
    print("------------------------------------")

    while sum_return_dealer(dealers_cards) < 17:
        dealers_cards.append(random.sample(card_stack, 1))
        print("Dealer's Cards --> {} --> {}".format(dealers_cards, sum_return_dealer(dealers_cards)))
    print("--------------------------------------------------------")

    print("Your Cards --> {} --> {}".format(my_cards, sum_return_self(my_cards))) 
    print("Delaers Cards --> {} --> {}".format(dealers_cards, sum_return_dealer(dealers_cards)))
    print("--------------------------------------------------------")
    
    if sum_return_dealer(dealers_cards) > 21:
        print("It's a BUST. You WIN, Dealer Loses!")
    elif sum_return_dealer(dealers_cards) > sum_return_self(my_cards):
        print("Dealer Wins!")
    elif sum_return_dealer(dealers_cards) == sum_return_self(my_cards):
        print("PUSH! It's a draw.")
    else:
        print("You Win!")