from re import fullmatch

vehicle_number=input("Enter the vehicle number : ")

pattern="(KL)\d{2}[A-Z]{1,2}\d{4}"

matcher=fullmatch(pattern,vehicle_number)

if matcher==None:

    print("invalid")

else:

    print("valid")
