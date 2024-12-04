from re import fullmatch

mobile_number=input("Enter the mobile number : ")

pattern="[+]?(91)?\d{10}"

matcher=fullmatch(pattern,mobile_number)

if matcher==None:

    print("Invalid")

else:

    print("valid")