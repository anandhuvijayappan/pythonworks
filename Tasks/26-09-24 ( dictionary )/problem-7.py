# 7. Write a Python program to filter a dictionary, keeping only items with values greater than 50 using dictionary comprehension.

input_dict = {'a': 45,'b': 67,'c': 23,'d': 89,'e': 50,'f': 91}

dictionary = {i:j for i,j in input_dict.items() if j>50}

print(dictionary)