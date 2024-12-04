#Python program to count the occurrences of each element in a list

lst=[1,5,3,7,8,9,0,8,6,3,5,8,5,4,3,6]

for i in range(0,len(lst)):

    count=0

    new=True

    for k in range(0,i):

        if lst[k]==lst[i]:

            new=False

    if new==True:

        for j in range(0,len(lst)):

            if lst[i]==lst[j]:

                count=count+1

        print("Element :  ",lst[i]," - Occurrences :  ",count)