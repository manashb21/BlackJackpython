import random
from sum_return import *

card_stack = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K')

def stand(my_cards, dealers_cards):
    dealers_cards.append(random.sample(card_stack, 1))
    
    print("Your Cards --> {} --> {}".format(my_cards, sum_return_self(my_cards))) 
    print("Delaers Cards --> {} --> {}".format(dealers_cards, sum_return_dealer(dealers_cards)))

    if sum_return_dealer(dealers_cards) > sum_return_self(my_cards):
        print("Dealer Wins!")
    elif sum_return_dealer(dealers_cards) == sum_return_self(my_cards):
        print("PUSH! It's a draw.")
    else:
        print("You Win!")