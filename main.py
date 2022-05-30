import random

card_stack = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K')
my_cards = []
dealers_cards = []

def draw():
    print("  -------------------- ")
    print("~ Welcome to BlackJack ~")
    print("  -------------------- ")
    print("\nFirst Deal")
    print("------------")
    my_cards.append(random.sample(card_stack, 2))
    dealers_cards.append(random.sample(card_stack, 1))

    print("Your Cards --> {} --> {}".format(my_cards, sum_return_self(my_cards)))
    print("Dealer's Cards --> {} --> {}".format(dealers_cards, sum_return_dealer(dealers_cards)))
    print("--------------------------")

    if sum_return_self(my_cards) == 21:
        print("~~~~!! BLACKJACK !!~~~")
        stand(my_cards, dealers_cards)
    else:
        print("\nWhat do you want to do?")
        print("\nHIT(h) | STAND(s)")
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

def hit(my_cards, dealers_cards):
    my_cards.append(random.sample(card_stack, 1))
    dealers_cards.append(random.sample(card_stack, 1))
    print("Your Cards --> {} --> {}".format(my_cards, sum_return_self(my_cards))) 
    print("Delaers Cards --> {} --> {}".format(dealers_cards, sum_return_dealer(dealers_cards)))    
    if sum_return_self(my_cards) > 21:
        print("It's a BUST. You LOSE! ~~ Dealer Wins!!")
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
    
def sum_return_self(my_cards):    
    count = 0
    for i in my_cards:
        for j in i:
            if j == 'A':
                count += 11
            elif (j == "J") ^ (j == "Q") ^ (j == 'K'):
                count += 10
            else:
                count += j
    return count
  


def sum_return_dealer(dealers_cards):
    count = 0
    for i in dealers_cards:
        for j in i:
            if j == 'A':
                count += 11
            elif (j == "J") ^ (j == "Q") ^ (j == 'K'):
                count += 10
            else:
                count += j
    return count

def dealer_autohit():
    return 1


draw()