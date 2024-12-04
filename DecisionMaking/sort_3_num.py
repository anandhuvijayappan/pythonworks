num1=int(input("Enter the first number  : "))

num2=int(input("Enter the second number : "))

num3=int(input("Enter the third number  : "))

if num1<num2<num3 :

    print("Sorted : ",num1,num2,num3)

elif num3<num2<num1 :

    print("Sorted : ",num3,num2,num1)

elif num2<num3<num1 :

    print("Sorted : ",num2,num2,num1)

elif num1<num3<num2 :

    print("Sorted : ",num1,num3,num2)

elif num3<num1<num2 :

    print("Sorted : ",num3,num1,num2)

elif num2<num1<num3 :

    print("Sorted : ",num2,num1,num3)