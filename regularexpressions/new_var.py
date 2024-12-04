from re import fullmatch #fullmatch is using for checking the exact match

user_input=input("Enter the variable name : ")




pattern="[p-t][369][0-9a-zA-Z]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:

    print("valid")
