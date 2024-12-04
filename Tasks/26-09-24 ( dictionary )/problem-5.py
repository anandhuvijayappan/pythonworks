#5. Write a Python program to create a dictionary from a list of keys and values using dictionary comprehension.

keys = ['name', 'age', 'city']

values = ['Alice', 30, 'New York']

dictionary={keys[i]:values[i] for i in range(0,len(keys))}

print(dictionary)