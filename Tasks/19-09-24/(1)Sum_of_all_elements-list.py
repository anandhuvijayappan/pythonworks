#Python program to find the sum of all elements in a list.

lst=[1,2,3,4,5,6,7,8,9,10]

sum=0

for i in range(0,len(lst)):

    sum=sum+lst[i]

print("Sum of all elements in the list is : ",sum)