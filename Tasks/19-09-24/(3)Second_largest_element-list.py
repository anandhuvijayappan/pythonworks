#Python program to find the second largest element in a list.

lst=[1,3,4,9,0,4]

lar=0

sec_lar=0

for i in range(0,len(lst)):

    zero=False

    if lar<lst[i]:

        sec_lar=lar

        lar=lst[i]

    elif lar>lst[i]>sec_lar:

        sec_lar=lst[i]

print("Second largest element is : ",sec_lar)



