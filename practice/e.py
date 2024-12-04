list1=[]

length=int(input("Enter the length of the list : "))

print("Enter the elements of the list : ")

for i in range(0,length):
     
     list1[i]=int(input("index : ",i," : "))

un=set()

for i in range(0,len(list1)):

    flag=True

    for j in un:

        if list1[i]==j:

            flag=False

    if flag==True:

            count=0

            
            for j in range(i,len(list1)):


                if list1[i]==list1[j]:

                    count=count+1

            print("Count ",list1[i]," : ", count)

            un.add(list1[i])

            
        

        
