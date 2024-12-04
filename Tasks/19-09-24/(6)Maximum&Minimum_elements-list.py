#Python program to find the maximum and minimum elements in a list.

lst=[2,4,5,6,8,5,7,4,6,7,8,9,6,5,4,3]

#Maximum

for i in range(0,len(lst)-1):

    if lst[i]>lst[i+1]:

        temp=lst[i]

        lst[i]=lst[i+1]

        lst[i+1]=temp

print("Maximum element : ",lst[len(lst)-1])

#Minimum

for i in range(len(lst)-2,-1,-1):

    if lst[i]>lst[i+1]:

        temp=lst[i]

        lst[i]=lst[i+1]

        lst[i+1]=temp

print("Minimum element : ",lst[0])