# is_perfect_number(number)

def is_perfect_number(number):
    
    sum=0
    
    for i in range(1,(number//2)+1):
        
        if number%i==0:
            
            sum=sum+i
            
    if number==sum:
        
        print(number," is a perfect number")
        
    else:
        
        print(number," is not a perfect number")
        

# is_armstrong_number(number)

def is_armstrong_number(number):
    
    temp=number
    
    digit=0
    
    while temp!=0:
        
        temp=temp//10

        
        digit=digit+1
        
    temp=number
    
    sum=0
    
    while temp!=0:
        
        sum=sum+((temp%10)**digit)     
        temp=temp//10   
        
    if number==sum:
        
        print(number," is a armstrong number")
        
    else:
        
        print(number," is not a armstrong number")

# is_palindrome_number(number)

def is_palindrome_number(number):

    temp=number
    rebmun=0
    
    while temp!=0:

        rebmun=(rebmun*10)+(temp%10)
        
        temp=temp//10
    if number==rebmun:
        
        print(number," is a palindrome number")
        
    else:
        
        print(number," is not a palindrome number")

    





number=(int(input("Enter the number : ")))

print(" ")

is_perfect_number(number)

is_armstrong_number(number)

is_palindrome_number(number)

print(" ")