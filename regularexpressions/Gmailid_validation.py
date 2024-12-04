from re import fullmatch

user_input=input("Enter the G-mail id : ")

pattern="[a-z]{1}[a-z0-9]{0,63}[@](gmail.com)"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invlid")

else:

    print("Valid")