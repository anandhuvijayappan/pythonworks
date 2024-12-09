
def loop_fn(t_number):

    sum_of_sq=0

    while t_number!=0:

        digit=t_number%10

        t_number=t_number//10

        sum_of_sq += (digit**2) 

    return sum_of_sq


number=32

loop_count=1

print(loop_fn(number))

r_number=loop_fn(number)



while r_number!=1 and loop_count!=0:

    r_number=loop_fn(r_number)

    print(r_number)

    if r_number==4:

        loop_count -= 1




