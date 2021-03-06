import random
from sum_return import *
from stand import stand

card_stack = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K') 

def hit(my_cards, dealers_cards):
    my_cards.append(random.sample(card_stack, 1))
    dealers_cards.append(random.sample(card_stack, 1))
    
    print("Your Cards --> {} --> {}".format(my_cards, sum_return_self(my_cards))) 
    print("Delaers Cards --> {} --> {}".format(dealers_cards, sum_return_dealer(dealers_cards)))  

    if sum_return_self(my_cards) == sum_return_dealer(dealers_cards):
        print("It is a DRAW.")  
    
    while sum_return_dealer(dealers_cards) < 17:
        dealers_cards.append(random.sample(card_stack, 1))
        print("Dealer's Cards --> {} --> {}".format(dealers_cards, sum_return_dealer(dealers_cards)))

    if sum_return_self(my_cards) > 21:
        print("It's a BUST. You LOSE! ~~ Dealer Wins!!")
    elif sum_return_dealer(dealers_cards) > 21:
        print("It's a BUST. You WIN! ~~ Dealers Looses!!")
    else:
        print("\nWhat do you want to do? HIT(h) STAND (s)")
        option_select = str(input())
        if (option_select == 'h') ^ (option_select == 'H'):
            print("--------------------")
            print("You chose to HIT.")
            print("--------------------")
            hit(my_cards, dealers_cards)
        elif (option_select == 's') ^ (option_select == 'S'):
            print("--------------------")
            print("You chose to STAND.")
            print("--------------------")
            stand(my_cards, dealers_cards) 