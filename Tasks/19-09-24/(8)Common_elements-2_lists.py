#Python program to find common elements in two lists.

list1=[1,3,4,5,6,7,9,6]

list2=[2,4,5,6,8,6]

common=[]

for i in range(0,len(list1)):

    count=0

    new=True

    for k in range(0,i):

        if list1[k]==list1[i]:

            new=False

    if new==True:

        for j in range(0,len(list2)):

            if list1[i]==list2[j]:

                common.insert(len(common),list1[i])

                break



if len(common)==0:

    print("There are no common elements here !!")

else:

    for x in range(0,len(common)):

        print(common[x])

    print("These are the commen elements of the two lists ",list1," and ",list2,".")