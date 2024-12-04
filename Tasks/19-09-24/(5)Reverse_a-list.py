#Python program to reverse a list.

lst=[1,2,3,4,5]

print("List          : ",lst)

rev_lst=[]

for i in range(0,len(lst)):

    rev_lst.insert(0,lst.pop(0))

print("Reversed list : ",rev_lst)