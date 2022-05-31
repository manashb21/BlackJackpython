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
