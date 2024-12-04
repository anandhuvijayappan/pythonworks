# 1.Write and Read a File:
#   - Write a program to take input from the user and write it to a file. Then, read the content from the file and display it.

f1=open("P:\Luminar\pythonworks\dataset\problem-1_08-10-2024.txt","w")

f2=open("P:\Luminar\pythonworks\dataset\problem-1_08-10-2024.txt")

text=input("Enter some text to write to the file : ")

f1.write(text)

print(f2)

f1.close()

f2.close()


