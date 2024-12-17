def is_palindrome(number):

    str_num=str(number)

    rev_num = str_num[::-1]

    if str_num==rev_num:

        return True
    
    else:
        
        return False

def is_prime(number):

    prime=True

    if number<2:

        return False

    for i in range(2,((number+1)//2)+1):

        if number%i==0:

            prime=False

    return prime



n = 13

two_chk=False

number=n

while two_chk==False:

    if is_palindrome(number)==True and is_prime(number)==True:

        print(number)

        two_chk=True
    
    else:

        number+=1