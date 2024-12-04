
sentence = "Hello world! This is a test for finding the longest word."

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '=', '+', '{', '}', '[', ']', '|','\\',':', ';', '"', "'", '<', '>', ',', '.', '?', '/','`', '~']

words = sentence.split()

longest_word=""

length=0

for word in words:

    l_count=0

    for l in word:

        l_count+=1

    for sc in special_characters:

        word=word.replace(sc,"")


    if l_count>length:

        length=l_count

        longest_word=word

print("The longest word is : ",longest_word)

print("Length of the word : ",length)

    

