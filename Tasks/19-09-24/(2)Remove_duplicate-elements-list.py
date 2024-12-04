#Python program to remove duplicates from a list.

lst=[5, 3, 1, 2, 3, 1]

rm=[]

for i in range(0,len(lst)):

    for j in range(i+1,len(lst)):

        if lst[i]==lst[j]:

            flag=True

            for k in rm:

                if j==k:

                    flag=False

            if flag==True:

                rm.insert(0,j)

for p in rm:

    lst.pop(p)

print("Result -> ",lst)