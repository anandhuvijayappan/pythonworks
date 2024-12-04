#Python program to replace an element in a list with another element

list1=[1,3,5,7,9,8,6,4,2]

print(" list : ",list1)

print("You can replace an elements with index.")

print(" hint:")

print("    Index   Element ")

nd=", "

for i in range(0,len(list1)):

    if i == len(list1)-1:

        nd=""

    print("     ",i,"  -  ",list1[i])

index=int(input("Select the element that you want to replece by using its index : "))

print("Selected the element ",list1[index]," with index ",index)

element=int(input("Enter the element that you want to replace with                : "))

list1[index]=element

print("     Result -> ",list1)