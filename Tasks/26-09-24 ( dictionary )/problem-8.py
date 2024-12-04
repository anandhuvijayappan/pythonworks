# 8. Given a sentence, count the frequency of each word using a dictionary.

sentence = "A journey of a thousand miles begins with a single step"

words=sentence.split()

frequency={i:words.count(i) for i in words}

print(frequency)