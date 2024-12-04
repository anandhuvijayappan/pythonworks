# 1. Create a dictionary to store the names and ages of 5 people. Access and print the age of one person using their name.

people={"syam":32,"sigha":23,"sundar":28,"badri":26}

name=input("Enter the name : ")

print("Age            : ",people.get(name))