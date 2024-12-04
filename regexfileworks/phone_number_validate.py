from re import fullmatch

f=open("P:\\Luminar\\pythonworks\\regexfileworks\\phone_number_validate.txt")

for number in f:

    number=number.strip()

    pattern="[+]?(91)?\d{10}"

    matcher=fullmatch(pattern,number)

    if matcher!=None:

        print(number)