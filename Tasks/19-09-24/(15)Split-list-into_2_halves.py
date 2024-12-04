#Python program to split a list into two halves

list1=[1,3,5,7,9,8,6,4,2]

l_half=[]

r_half=[]

mid_index=(len(list1)-1)//2

for i in range(0,len(list1)):
    
    if i<=mid_index:

        l_half.insert(len(l_half),list1[i])

    elif i>mid_index:

        r_half.insert(len(r_half),list1[i])

print("Parent list : ",list1)

print("First half  : ",l_half)

print("Second half : ",r_half)