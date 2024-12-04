from re import fullmatch

f=open("P:\\Luminar\\pythonworks\\regexfileworks\\find_hashtags.txt")

for i in f:

    words=i.split(" ")

    for word in words:

        word=word.strip()

        pattern="[#]{1}[\w]*"

        matcher=fullmatch(pattern,word)

        if matcher!=None:

            print(word)

f.close()