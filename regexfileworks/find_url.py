from re import findall

f=open("P:\\Luminar\\pythonworks\\regexfileworks\\find_url.txt")

content=f.read()

print(content)

pattern="https?://[\w\S.]*"

urls=findall(pattern,content)

for url in urls:

    print(url)

        

f.close()