#Python program to find all the even numbers in a list.

list1=[1,3,5,7,9,8,6,4,2]

even=[]

for i in range(0,len(list1)):

    if list1[i]%2==0:

        even.insert(len(even),list1[i])

print("List of even numbers : ",even)