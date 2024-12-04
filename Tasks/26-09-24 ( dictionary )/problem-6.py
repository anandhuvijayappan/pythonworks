# 6. Given two lists, one with fruits and the other with prices, write a dictionary comprehension to pair them together into a dictionary.


fruits = ["apple", "banana", "cherry"]

prices = [100, 50, 150]

dictionary={fruits[i]:prices[i] for i in range(0,len(fruits))}

print(dictionary)