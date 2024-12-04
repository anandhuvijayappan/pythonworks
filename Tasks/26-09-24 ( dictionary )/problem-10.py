# 10. Given a dictionary of items and their prices, write a program to apply a 10% discount to all the items using dictionary comprehension.

items_dict = {'apple': 100,'banana': 50,'cherry': 75,'date': 120}

discount_price={i:j-((j/100)*10) for i,j in items_dict.items()}

print(discount_price)