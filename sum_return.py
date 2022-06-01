def sum_return_self(my_cards):    
    count = 0
    flag_for_A = 0
    for i in my_cards:
        for j in i:
            if j == 'A':
                flag_for_A += 1
            elif (j == "J") ^ (j == "Q") ^ (j == 'K'):
                count += 10
            else:
                count += j

    if count > 10 and flag_for_A > 0:
        count = count + flag_for_A
    elif count <= 10 and flag_for_A > 0:
        count = count + (flag_for_A * 11)
    return count
  
def sum_return_dealer(dealers_cards):
    count = 0
    flag_for_A = 0
    for i in dealers_cards:
         for j in i:
            if j == 'A':
                flag_for_A += 1
            elif (j == "J") ^ (j == "Q") ^ (j == 'K'):
                count += 10
            else:
                count += j

    if count > 10 and flag_for_A > 0:
        count = count + flag_for_A
    elif count <= 10 and flag_for_A > 0:
        count = count + (flag_for_A * 11)
    return count
