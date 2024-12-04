# employee id, name, dipartment, age, salary


employee={"id":100,"name":"seva","department":"hr","age":32,"salary":25000}

# approch to print a value using a key without error ( we can use  - print(employee["id"])  :-  but here an invalued key  )

print(employee.get("id"))

#fetch all keys from this dictionary

for k in employee.keys():

    print(k)

#fetch all values

for v in employee.values():

    print(v)

for i in employee.keys():

    print(i,"\t\t: ",employee.get(i))

