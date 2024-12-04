#input:
#x= int(input("Enter the number x : "))
#y= int(input("Enter the number y : "))
#z= int(input("Enter the number z : "))
#n= int(input("Enter the number n : "))

x=5
y=6
z=7
n=15

result=[]

for i in range(z,-1,-1):
    for j in range(x,-1,-1):
        for k in range(z,-1,-1):
            if i+j+k!=n:
                s=[i,j,k]
                result.insert(0,s)
                #print(set)

print("Result : ",result)