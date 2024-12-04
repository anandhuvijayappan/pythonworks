# 9. Write a dictionary comprehension to convert all the values in a dictionary to their absolute values.

dictionary = {'a': -1, 'b': -2, 'c': 3, 'd': -4}

result={i:j if j>0 else 0-j for i,j in dictionary.items()}

print(result)