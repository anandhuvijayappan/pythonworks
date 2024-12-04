number = int(input("Enter the number"))

number_a=0

number_b=1

number_f=0

if number_a==number :

    print(number ," is in the fibonacci series. ")

elif number_b==number :

    print(number ," is in the fibonacci series. ")


while (number<=number_f) :

    number_f=number_a+number_b

    if number_f==number :
        
        print(number ," is in the fibonacci series. ")

    number_a=number_b
    
    number_b=number_f