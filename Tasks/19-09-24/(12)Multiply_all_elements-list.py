#Python program to multiply all elements in a list.

list1=[1,3,5,7,9,8,6,4,2]

result=1

nd=" x "

for i in range(0,len(list1)):

    if i == len(list1)-1:

        nd=""

    result=result*list1[i-1]

    print(list1[i],end=nd)

print(" ->  : ",result)