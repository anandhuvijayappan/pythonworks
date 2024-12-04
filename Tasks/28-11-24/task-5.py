def max_profit(prices):

    min_value=min(prices)

    #print(min_value)

    min_index=prices.index(min_value)

    #print(min_index)

    max_value=0

    for i in range(min_index,len(prices)):

        if max_value<prices[i]:

            max_value=prices[i]
        
    profit=max_value-min_value

    return profit

prices=[7,1,5,3,6,4]

print(max_profit(prices))