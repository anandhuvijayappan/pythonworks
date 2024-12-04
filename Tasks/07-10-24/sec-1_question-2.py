# Next prime number

def is_prime(number):

    flag1=True

    if number==0 or number==1:

        flag1=False

    for i in range(2,(number//2)+1):

        if number%i==0:

            flag1=False

    return flag1

def next_prime(number):

    prime=0

    number=number+1

    prime=number

    while is_prime(number)==False:

        number=number+1

        prime=number

    return prime




#input

number=int(input("Enter the number : "))

#output

print("The next prime number is : ",next_prime(number))