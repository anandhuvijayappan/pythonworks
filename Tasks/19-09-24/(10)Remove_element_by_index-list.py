#Python program to remove an element from a list by index.

list1=[1,3,5,7,9,8,6,4,2]

print(" list : ",list1)

print(" You can remove elements by using the index of the element.")

print(" hint:")

print("       Element [index] -> ",end="")

nd=", "

for i in range(0,len(list1)):

    if i == len(list1)-1:

        nd=""

    print(list1[i],"[",i,"]",end=nd)

print("")

index=int(input(" Enter the index of the element : "))

if 0<=index<len(list1):

    removed=list1.pop(index)

    print(" Element ",removed," is removed")

    print(" list after removing the element -> ",list1)

else:

    print("Invalued index!")