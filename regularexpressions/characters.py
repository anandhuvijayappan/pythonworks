from re import finditer

text ="I have 3 Cars,Bike and 1-Cycle"

#pattern="[\w]" #"[a-zA-Z0-9]" Alphanumeric
#pattern="[\W]" #"[^a-zA-Z0-9]" exclude Alphanumeric
pattern="[\d]" #"[0-9]" digits
#pattern="[\D]" #"[^0-9]" exclude digits 
matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())

