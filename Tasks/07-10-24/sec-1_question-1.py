# Write a Python program that reads an integer from the user and performs the
# following checks:
# 1.If the number is divisible by 3, print "PING".
# 2.If the number is divisible by 5, print "PONG".
# 3.If the number is divisible by 15, print "PINGPONG".
# 4.If the number is not divisible by 3 or 5, print the number itself

number=int(input("Enter the number : "))

flag1=True

flag2=True

if number%3==0:

    print("PING")

else :
    
    flag1=False

if number%5==0:

    print("PONG")

else :
    
    flag2=False

if number%15==0:

    print("PINGPONG")

if flag1==False:

    print(number)
    
if flag2==False:

    print(number)