#Python program to merge two lists and sort the resulting list.

list1=[1,3,5,7,9]

list2=[2,4,6,8]

print("first list  : ",list1)

print("Second list : ",list2)

#merging

result=list1+list2

#sorting

for i in range(0,len(result)-1):

    for i in range(0,len(result)-1):

        if result[i]>result[i+1]:

            temp=result[i]

            result[i]=result[i+1]

            result[i+1]=temp

print("->   result : ",result)